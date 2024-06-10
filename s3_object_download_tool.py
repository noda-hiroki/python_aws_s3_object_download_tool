import logging
import boto3
from botocore.exceptions import ClientError
import os

def download_file(bucket, object_name, path):
    os.chdir(path)
    file_name = object_name
    s3_client = boto3.client("s3")
    try:
        response = s3_client.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
