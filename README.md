<h1 align="center">
	<a href="https://github.com/WolfSoftware">
		<img src="https://raw.githubusercontent.com/WolfSoftware/branding/master/images/general/banners/64/black-and-white.png" alt="Wolf Software Logo" />
	</a>
	<br>
	List all AWS regions
</h1>


<p align="center">
	<a href="https://travis-ci.com/AWSToolbox/list-regions">
		<img src="https://img.shields.io/travis/com/AWSToolbox/list-regions/master?style=for-the-badge&logo=travis" alt="Build Status">
	</a>
	<a href="https://github.com/AWSToolbox/list-regions/releases/latest">
		<img src="https://img.shields.io/github/v/release/AWSToolbox/list-regions?color=blue&style=for-the-badge&logo=github&logoColor=white&label=Latest%20Release" alt="Release">
	</a>
	<a href="https://github.com/AWSToolbox/list-regions/releases/latest">
		<img src="https://img.shields.io/github/commits-since/AWSToolbox/list-regions/latest.svg?color=blue&style=for-the-badge&logo=github&logoColor=white" alt="Commits since release">
	</a>
	<a href="LICENSE.md">
		<img src="https://img.shields.io/badge/license-MIT-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" alt="Software License">
	</a>
	<br>
	<a href=".github/CODE_OF_CONDUCT.md">
		<img src="https://img.shields.io/badge/Code%20of%20Conduct-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
	<a href=".github/CONTRIBUTING.md">
		<img src="https://img.shields.io/badge/Contributing-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
	<a href=".github/SECURITY.md">
		<img src="https://img.shields.io/badge/Report%20Security%20Concern-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
	<a href=".github/SUPPORT.md">
		<img src="https://img.shields.io/badge/Get%20Support-blue?style=for-the-badge&logo=read-the-docs&logoColor=white" />
	</a>
</p>

## Overview

This script will display a list of all available regions along with their location and your opt-in status.

### Installation

Once you have cloned the code you will need to install the required python packages.

```
pip install -r requirements.txt 
```
> The requirements file is in the src directory

### Usage

```shell
./list-regions.py
```

### Requirements

You will need a valid set of AWS credentials in order to run this command.

### Example output

```
+----------------+---------------------------+---------------------+
|  Region Name   |          Location         |        Status       |
+----------------+---------------------------+---------------------+
|   af-south-1   |     Africa (Cape Town)    |     not opted in    |
|   ap-east-1    |  Asia Pacific (Hong Kong) |     not opted in    |
| ap-northeast-1 |    Asia Pacific (Tokyo)   | opt in not required |
| ap-northeast-2 |    Asia Pacific (Seoul)   | opt in not required |
|   ap-south-1   |   Asia Pacific (Mumbai)   | opt in not required |
| ap-southeast-1 |  Asia Pacific (Singapore) | opt in not required |
| ap-southeast-2 |   Asia Pacific (Sydney)   | opt in not required |
|  ca-central-1  |      Canada (Central)     | opt in not required |
|  eu-central-1  |     Europe (Frankfurt)    | opt in not required |
|   eu-north-1   |     Europe (Stockholm)    | opt in not required |
|   eu-south-1   |       Europe (Milan)      |     not opted in    |
|   eu-west-1    |      Europe (Ireland)     | opt in not required |
|   eu-west-2    |      Europe (London)      | opt in not required |
|   eu-west-3    |       Europe (Paris)      | opt in not required |
|   me-south-1   |   Middle East (Bahrain)   |     not opted in    |
|   sa-east-1    | South America (Sao Paulo) | opt in not required |
|   us-east-1    |  US East (North Virginia) | opt in not required |
|   us-east-2    |       US East (Ohio)      | opt in not required |
|   us-west-1    |   US West (California)    | opt in not required |
|   us-west-2    |      US West (Oregon)     | opt in not required |
+----------------+---------------------------+---------------------+
```

## Availability Zones

If you want information relating to availability zones then please have a look at out [List Availability Zones](https://github.com/AWSToolbox/list-availability-zones) script.

> Listing availability zones only runs a **LOT** slower, so please make sure you select the correct script.

## Contributors

<p>
	<a href="https://github.com/TGWolf">
		<img src="https://img.shields.io/badge/Wolf-black?style=for-the-badge" />
	</a>
</p>

## Show Support

<p>
	<a href="https://ko-fi.com/wolfsoftware">
		<img src="https://img.shields.io/badge/Ko%20Fi-blue?style=for-the-badge&logo=ko-fi&logoColor=white" />
	</a>
</p>
