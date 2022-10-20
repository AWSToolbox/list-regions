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


def main(_cmdline=None) -> None:

    """
    The main function. This takes the command line arguments provided and parse them.
    """

    country_mapping = get_country_mapping()
    print(country_mapping)

def get_country_mapping():
    """
    something here
    """

    ssm = boto3.client('ssm')

    regions = {}
    for nsc in get_region_short_codes(ssm):
        regions[nsc] = get_region_long_name(ssm, nsc)

    sorted_regions = dict(sorted(regions.items()))

    return sorted_regions


def get_region_long_name(ssm, short_code):
    """
    something here
    """

    response = ssm.get_parameters(Names=[f'/aws/service/global-infrastructure/regions/{short_code}/longName'])
    return response['Parameters'][0]['Value']

def get_region_short_codes(ssm):
    """
    something here
    """

    output = set()
    for page in ssm.get_paginator('get_parameters_by_path').paginate(
        Path='/aws/service/global-infrastructure/regions'
    ):
        output.update(p['Value'] for p in page['Parameters'])

    return output

if __name__ == "__main__":
    main(sys.argv[1:])
