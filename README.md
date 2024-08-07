## Automated S3 Folder Cleanup Data Engineering Script

This repository contains an automation script developed on the Mage.ai platform. The script is responsible for listing and deleting objects in a specific folder within an S3 bucket on AWS. Below, we detail each important section to understand and use this script.

### Overview

The `cleanup_s3_folder.py` script, located in the `data_pipeline_scripts` folder, automates the cleanup of a specific folder in an S3 bucket. It lists all objects present in the folder and deletes them, facilitating the maintenance and organization of data stored in S3.

### Problem Description

When working with large volumes of data in data lakes on S3, it is often necessary to perform cleanup and maintenance operations, such as deleting old or unnecessary files. Doing this manually can be time-consuming and error-prone. This script automates the process of listing and deleting objects in a specific S3 folder, ensuring efficient and secure data management.
