"""
This module provides a function to display AWS region information in a table format.

The `display_results` function takes a list of dictionaries containing AWS region information and
displays it using the PrettyTable library. Each dictionary in the list should contain the keys
'RegionName', 'Location', 'STATUS'. The table is sorted by the 'Region Name' field
before being printed.

Dependencies:
    - prettytable: A library for creating simple ASCII tables

Usage Example:
    results = [
        {
            'RegionName': 'us-east-1',
            'Location': 'North Virginia',
            'STATUS': 'opted-in'
        },
        {
            'RegionName': 'us-west-1',
            'Location': 'California',
            'STATUS': 'not-opted-in'
        }
    ]
    display_results(results)
"""

from typing import Any, Dict, List
from prettytable import PrettyTable


def display_results(results: List[Dict[str, Any]]) -> None:
    """
    Display the results in a table format.

    Arguments:
        results (List[Dict[str, Any]]): The list of dictionaries containing AWS region information to display.
                                        Each dictionary should have the keys 'RegionName', 'Location', and 'STATUS'.
    """
    table = PrettyTable(field_names=['Region Name', 'Location', 'Status'])
    for parts in results:
        table.add_row([parts['RegionName'], parts['Location'], parts['STATUS']])
    table.sortby = 'Region Name'
    print(table)
