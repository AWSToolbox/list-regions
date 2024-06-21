"""
This module provides functions to generate and display a list of AWS regions.

It retrieves region information from AWS SSM and EC2 services. Threading is used to parallelize API calls for improved performance.

Functions:
    get_regions: Generates and returns the region zone list.
    create_boto3_session: Creates a boto3 session using the specified authentication method.
    get_country_mapping: Retrieves a mapping of AWS region short codes to their long names.
    get_region_long_name: Retrieves the long name of a region given its short code.
    get_region_short_codes: Retrieves a set of region short codes.
    query_api: Queries the AWS API to get a list of regions.

Dependencies:
    - boto3: AWS SDK for Python
    - botocore: Low-level, data-driven core of boto3
    - yaspin: A lightweight terminal spinner
"""

from typing import Any, Dict, List, Set
import concurrent.futures
from types import SimpleNamespace

import boto3  # type: ignore pylint: disable=import-error
from botocore.exceptions import ClientError, BotoCoreError  # type: ignore pylint: disable=import-error

from yaspin import yaspin

from .exceptions import AWSRegionsError


def get_regions(config: SimpleNamespace) -> List[Dict[str, Any]]:
    """
    Generate and returns the region list.

    Arguments:
        config (SimpleNamespace): Configuration object containing necessary settings.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with region information.
    """
    try:
        country_mapping: Dict[str, str] = get_country_mapping(config)
    except (ClientError, BotoCoreError) as e:
        raise AWSRegionsError(f"Failed to get country mapping: {str(e)}") from e

    try:
        session: Any = create_boto3_session(config)
        client: Any = session.client('ec2')

        with yaspin(text="Generating Region List", color="cyan") as spinner:
            try:
                results: List[Dict[str, Any]] = query_api(client, country_mapping)
            except AWSRegionsError as e:
                spinner.fail("Failed")
                raise e
            spinner.ok("Complete")
        return results
    except AWSRegionsError as e:
        raise AWSRegionsError(f"Failed to get regions: {e}") from e


def create_boto3_session(config: SimpleNamespace) -> boto3.Session:
    """
    Create a boto3 session using the specified authentication method.

    Arguments:
        config (SimpleNamespace): Configuration object containing parsed command line arguments.

    Returns:
        boto3.Session: A boto3 session object
    """
    try:
        if config.profile:
            return boto3.Session(profile_name=config.profile)
        return boto3.Session()
    except (BotoCoreError, ClientError) as e:
        raise AWSRegionsError(f"Failed to create boto3 session: {e}") from e


def get_country_mapping(config: SimpleNamespace) -> Dict[str, str]:
    """
    Fetch a mapping of AWS region short codes to their long names concurrently.

    Returns:
        Dict[str, str]: A dictionary where keys are region short codes and values are their corresponding long names.
    """
    ssm: Any = boto3.client('ssm')
    region_short_codes: Set[str] = get_region_short_codes(ssm)
    regions: Dict = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=config.threads) as executor:
        futures: Dict[concurrent.futures.Future[str], str] = {executor.submit(get_region_long_name, ssm, nsc): nsc for nsc in region_short_codes}
        for future in concurrent.futures.as_completed(futures):
            nsc: str = futures[future]
            try:
                regions[nsc] = future.result()
            except (ClientError, BotoCoreError) as e:
                regions[nsc] = "unknown"
                print(f"Error fetching long name for {nsc}: {str(e)}")

    return dict(sorted(regions.items()))


def get_region_long_name(ssm, short_code: str) -> str:
    """
    Retrieve the long name of a region given its short code.

    Arguments:
        ssm (boto3.client): Boto3 SSM client.
        short_code (str): Short code of the region.

    Returns:
        str: Long name of the region.

    Raises:
        ClientError: If there is an error fetching the parameter from SSM.
    """
    param_name: str = f'/aws/service/global-infrastructure/regions/{short_code}/longName'
    response: Any = ssm.get_parameter(Name=param_name)
    return response['Parameter']['Value']


def get_region_short_codes(ssm) -> Set[str]:
    """
    Retrieve a set of all region short codes.

    Arguments:
        ssm (boto3.client): Boto3 SSM client.

    Returns:
        Set[str]: A set of region short codes.

    Raises:
        ClientError: If there is an error fetching the parameters from SSM.
    """
    paginator: Any = ssm.get_paginator('get_parameters_by_path')
    output = set()
    try:
        for page in paginator.paginate(Path='/aws/service/global-infrastructure/regions'):
            output.update(p['Value'] for p in page['Parameters'])
    except (ClientError, BotoCoreError) as e:
        print(f"Error fetching region short codes: {str(e)}")
    return output


def query_api(client, country_mapping: Dict[str, str]) -> List[Dict[str, Any]]:
    """
    Query the AWS EC2 API to get regions and their opt-in statuses.

    Arguments:
        client (boto3.client): Boto3 EC2 client.
        country_mapping (Dict[str, str]): Dictionary mapping region short codes to their long names.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing region information.

    Raises:
        AWSRegionsError: If there is an error querying the EC2 API.
    """
    results: List = []
    try:
        response: Any = client.describe_regions(AllRegions=True)
    except (ClientError, BotoCoreError) as e:
        raise AWSRegionsError(f"Error querying EC2 API: {str(e)}") from e

    if 'Regions' in response:
        for region in response['Regions']:
            my_region_name: Any = region['RegionName']
            status: Any = region['OptInStatus'].replace('-', ' ')
            location: str = country_mapping.get(my_region_name, "unknown")
            results.append({'RegionName': my_region_name, 'Location': location, 'STATUS': status})

    return results
