import logging
from mage_ai.settings.repo import get_repo_path
from os import path
import boto3
from mage_ai.data_preparation.shared.secrets import get_secret_value

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_s3_client():
    """Initialize and return an S3 client using AWS credentials."""
    aws_access_key_id = get_secret_value('aws_access_key_id')
    aws_secret_access_key = get_secret_value('aws_secret_access_key')
    return boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def list_objects_in_folder(s3, bucket_name, folder_prefix):
    """List objects in the specified S3 folder."""
    try:
        response = s3.list_objects(Bucket=bucket_name, Prefix=folder_prefix)
        return response.get('Contents', [])
    except boto3.exceptions.Boto3Error as e:
        logging.error(f"Error listing objects in S3: {e}")
        return []

def delete_objects_in_folder(s3, bucket_name, objects):
    """Delete specified objects in the S3 folder."""
    for obj in objects:
        try:
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            logging.info(f"Deleted: {obj['Key']}")
        except boto3.exceptions.Boto3Error as e:
            logging.error(f"Error deleting object {obj['Key']}: {e}")

@data_loader
def load_data(*args, **kwargs):
    """Main function to load and process data."""
    s3 = initialize_s3_client()
    
    config_path = path.join(get_repo_path(), 'config.yaml')
    config_profile = 'default'
    bucket_name = 'data-lake'
    folder_prefix = 'example_folder/'
    
    objects = list_objects_in_folder(s3, bucket_name, folder_prefix)
    
    if objects:
        delete_objects_in_folder(s3, bucket_name, objects)
    else:
        logging.info(f"No objects found in folder: {folder_prefix}")

    return {'status': 'success'}

@test
def test_output(output, *args) -> None:
    """Template code to test the block output."""
    assert output is not None, 'The output is undefined'
    assert output.get('status') == 'success', 'Failed to delete objects in S3'
