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

from typing import Any, Dict, List
from types import SimpleNamespace

from yaspin import yaspin

from wolfsoftware.get_aws_regions import get_region_list, RegionListingError

from .exceptions import AWSRegionsError


def get_regions(config: SimpleNamespace) -> List[Dict[str, Any]]:
    """
    Generate and returns the region list.

    Arguments:
        config (SimpleNamespace): Configuration object containing necessary settings.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with region information.
    """
    with yaspin(text="Retrieving Region List", color="cyan") as spinner:
        try:
            results: Any = get_region_list(all_regions=True, details=True, profile_name=config.profile)
        except RegionListingError as e:
            raise AWSRegionsError(f"Failed to get regions: {str(e)}") from e
        spinner.ok("Complete")
    return results
