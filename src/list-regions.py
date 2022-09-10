#!/usr/bin/env python
# pylint: disable=C0103

"""
This script will query the AWS API using boto3 and provide a list (table) of all regions and your current opt in status

Example Usage:

    ./list-regions.py
"""

from __future__ import print_function

import sys
import boto3

from botocore.exceptions import ClientError
from prettytable import PrettyTable

# pylint: disable=C0103
unknown_string = 'unknown'
country_mapping = {
                       'af-south-1': 'Africa (Cape Town)',
                       'ap-east-1': 'Asia Pacific (Hong Kong)',
                       'ap-south-1': 'Asia Pacific (Mumbai)',
                       'ap-northeast-2': 'Asia Pacific (Seoul)',
                       'ap-southeast-1': 'Asia Pacific (Singapore)',
                       'ap-southeast-2': 'Asia Pacific (Sydney)',
                       'ap-northeast-1': 'Asia Pacific (Tokyo)',
                       'ca-central-1': 'Canada (Central)',
                       'eu-central-1': 'Europe (Frankfurt)',
                       'eu-west-1': 'Europe (Ireland)',
                       'eu-west-2': 'Europe (London)',
                       'eu-west-3': 'Europe (Paris)',
                       'eu-north-1': 'Europe (Stockholm)',
                       'eu-south-1': 'Europe (Milan)',
                       'me-south-1': 'Middle East (Bahrain)',
                       'sa-east-1': 'South America (Sao Paulo)',
                       'us-east-2': 'US East (Ohio)',
                       'us-east-1': 'US East (North Virginia)',
                       'us-west-1': 'US West (California) ',
                       'us-west-2': 'US West (Oregon)',
                  }


def main(_cmdline=None) -> None:

    """
    The main function. This takes the command line arguments provided and parse them.
    """

    client = boto3.client('ec2')
    results = query_api(client)
    display_results(results)


def query_api(client):
    """
    Query the API
    """

    results = []

    try:
        response = client.describe_regions(AllRegions=True)
    except ClientError as e:
        print("Error: " + str(e))
    else:
        if 'Regions' in response:
            for region in response['Regions']:
                my_region_name = region['RegionName']
                status = region['OptInStatus'].replace('-', ' ')

                results.append({
                                'RegionName': my_region_name,
                                'Location': country_mapping[my_region_name] if my_region_name in country_mapping else unknown_string,
                                'STATUS': status,
                               })
    return results


def display_results(results):
    """
    Display the results
    """

    table = PrettyTable()

    table.field_names = [
                         'Region Name',
                         'Location',
                         'Status',
                        ]

    for parts in results:
        table.add_row([
                       parts['RegionName'],
                       parts['Location'],
                       parts['STATUS'],
                      ])

    table.sortby = 'Region Name'
    print(table)


if __name__ == "__main__":
    main(sys.argv[1:])
