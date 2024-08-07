## Automated S3 Folder Cleanup Data Engineering Script

This repository contains an automation script developed on the Mage.ai platform. The script is responsible for listing and deleting objects in a specific folder within an S3 bucket on AWS. Below, we detail each important section to understand and use this script.

### Overview

The `cleanup_s3_folder.py` script, located in the `data_pipeline_scripts` folder, automates the cleanup of a specific folder in an S3 bucket. It lists all objects present in the folder and deletes them, facilitating the maintenance and organization of data stored in S3.

### Problem Description

When working with large volumes of data in data lakes on S3, it is often necessary to perform cleanup and maintenance operations, such as deleting old or unnecessary files. Doing this manually can be time-consuming and error-prone. This script automates the process of listing and deleting objects in a specific S3 folder, ensuring efficient and secure data management.

### Objective

The objective of this script is to automate the cleanup of a specific folder in an S3 bucket by deleting all objects found in that folder. This is useful for keeping the data lake organized and avoiding unnecessary storage costs.

### Prerequisites

Before running this script, make sure you have:

- An AWS account with the necessary permissions to access and manipulate objects in S3.
- Mage.ai installed and configured on your machine.
- AWS credentials configured and securely stored to be accessed by the script.

### Installation

To set up the environment and run the script, follow the steps below:

1. Clone this repository:

```py
git clone https://github.com/nathadriele/S3-folder-cleanup.git
cd data_pipeline_scripts
```

2. Install the necessary dependencies (if you don't have Mage.ai and boto3 installed yet):

```py
pip install mage-ai boto3
```

3. Configure your AWS credentials in Mage.ai using the command:

```py
mage secret set aws_access_key_id=<your_access_key> aws_secret_access_key=<your_secret_key>
```
