<!-- markdownlint-disable -->
<p align="center">
    <a href="https://github.com/AWSToolbox/">
        <img src="https://cdn.wolfsoftware.com/assets/images/github/organisations/awstoolbox/black-and-white-circle-256.png" alt="AWSToolbox logo" />
    </a>
    <br />
    <a href="https://github.com/AWSToolbox/list-regions/actions/workflows/cicd.yml">
        <img src="https://img.shields.io/github/actions/workflow/status/AWSToolbox/list-regions/cicd.yml?branch=master&label=build%20status&style=for-the-badge" alt="Github Build Status" />
    </a>
    <a href="https://github.com/AWSToolbox/list-regions/blob/master/LICENSE.md">
        <img src="https://img.shields.io/github/license/AWSToolbox/list-regions?color=blue&label=License&style=for-the-badge" alt="License">
    </a>
    <a href="https://github.com/AWSToolbox/list-regions">
        <img src="https://img.shields.io/github/created-at/AWSToolbox/list-regions?color=blue&label=Created&style=for-the-badge" alt="Created">
    </a>
    <br />
    <a href="https://github.com/AWSToolbox/list-regions/releases/latest">
        <img src="https://img.shields.io/github/v/release/AWSToolbox/list-regions?color=blue&label=Latest%20Release&style=for-the-badge" alt="Release">
    </a>
    <a href="https://github.com/AWSToolbox/list-regions/releases/latest">
        <img src="https://img.shields.io/github/release-date/AWSToolbox/list-regions?color=blue&label=Released&style=for-the-badge" alt="Released">
    </a>
    <a href="https://github.com/AWSToolbox/list-regions/releases/latest">
        <img src="https://img.shields.io/github/commits-since/AWSToolbox/list-regions/latest.svg?color=blue&style=for-the-badge" alt="Commits since release">
    </a>
    <br />
    <a href="https://github.com/AWSToolbox/list-regions/blob/master/.github/CODE_OF_CONDUCT.md">
        <img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/AWSToolbox/list-regions/blob/master/.github/CONTRIBUTING.md">
        <img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/AWSToolbox/list-regions/blob/master/.github/SECURITY.md">
        <img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge" />
    </a>
    <a href="https://github.com/AWSToolbox/list-regions/issues">
        <img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge" />
    </a>
</p>

## Overview

This Python package allows you to list all availability zones configured for a given AWS account. It is part of our larger
[AWS Toolkit](https://github.com/AWSToolbox).

### Installation

To install the package, use:

```sh
pip install wolfsoftware.list-regions
```

### Usage

To list all regions for your AWS account, use the following command:

```sh
usage: list-regions [-h] [-V] [-p PROFILE] [-t THREADS]

List all regions configured for an account.

flags:
  -h, --help            Show this help message and exit
  -V, --version         Show program's version number and exit.

optional:
  -p PROFILE, --profile PROFILE
                        AWS profile name from ~/.aws/credentials (default: None)
  -t THREADS, --threads THREADS
                        The number of threads to use (default: 8)
```

### Requirements

You will need a valid set of AWS credentials to run this command. These credentials should be configured in your `~/.aws/credentials` file.

### Example Output

Below is an example of the output you can expect from running this command:

```
+----------------+---------------------------+---------------------+
|  Region Name   |          Location         |        Status       |
+----------------+---------------------------+---------------------+
|   af-south-1   |     Africa (Cape Town)    |     not opted in    |
|   ap-east-1    |  Asia Pacific (Hong Kong) |     not opted in    |
| ap-northeast-1 |    Asia Pacific (Tokyo)   | opt in not required |
| ap-northeast-2 |    Asia Pacific (Seoul)   | opt in not required |
| ap-northeast-3 |    Asia Pacific (Osaka)   | opt in not required |
|   ap-south-1   |   Asia Pacific (Mumbai)   | opt in not required |
|   ap-south-2   |  Asia Pacific (Hyderabad) |     not opted in    |
| ap-southeast-1 |  Asia Pacific (Singapore) | opt in not required |
| ap-southeast-2 |   Asia Pacific (Sydney)   | opt in not required |
| ap-southeast-3 |   Asia Pacific (Jakarta)  |     not opted in    |
| ap-southeast-4 |  Asia Pacific (Melbourne) |     not opted in    |
|  ca-central-1  |      Canada (Central)     | opt in not required |
|   ca-west-1    |   Canada West (Calgary)   |     not opted in    |
|  eu-central-1  |     Europe (Frankfurt)    | opt in not required |
|  eu-central-2  |      Europe (Zurich)      |     not opted in    |
|   eu-north-1   |     Europe (Stockholm)    | opt in not required |
|   eu-south-1   |       Europe (Milan)      |     not opted in    |
|   eu-south-2   |       Europe (Spain)      |     not opted in    |
|   eu-west-1    |      Europe (Ireland)     | opt in not required |
|   eu-west-2    |      Europe (London)      | opt in not required |
|   eu-west-3    |       Europe (Paris)      | opt in not required |
|  il-central-1  |     Israel (Tel Aviv)     |     not opted in    |
|  me-central-1  |     Middle East (UAE)     |     not opted in    |
|   me-south-1   |   Middle East (Bahrain)   |     not opted in    |
|   sa-east-1    | South America (Sao Paulo) | opt in not required |
|   us-east-1    |   US East (N. Virginia)   | opt in not required |
|   us-east-2    |       US East (Ohio)      | opt in not required |
|   us-west-1    |  US West (N. California)  | opt in not required |
|   us-west-2    |      US West (Oregon)     | opt in not required |
+----------------+---------------------------+---------------------+
```

### Additional Information

For more tools and utilities, check out our [AWS Toolkit](https://github.com/AWSToolbox).

<br />
<p align="right"><a href="https://wolfsoftware.com/"><img src="https://img.shields.io/badge/Created%20by%20Wolf%20on%20behalf%20of%20Wolf%20Software-blue?style=for-the-badge" /></a></p>
