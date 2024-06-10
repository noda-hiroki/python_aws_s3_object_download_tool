import logging
import boto3
from botocore.exceptions import ClientError
import os

bucket = input("bucket name:")
file = input("file name:")
path = input("Download path:")
s3_client = boto3.client("s3")
os.chdir(path)
try:
    s3_client.download_file(bucket, file, file)
except ClientError as e:
    logging.error(e)
os.system("PAUSE")
