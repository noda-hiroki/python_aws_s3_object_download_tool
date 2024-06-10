import logging
import boto3
from botocore.exceptions import ClientError
import os

#   バケット名、ファイル名、ダウンロード先のパスを入力
bucket = input("bucket name:")
file = input("file name:")
path = input("Download path:")
#   カレントディレクトリを、ダウンロード先ディレクトリに移動
os.chdir(path)

try:
    while True:
        select = input("Select whether to set an access key, secret access key, and region.(y/n):")
        if select == "y":
            #   アクセスキー、シークレットアクセスキー、リージョンを設定
            access_key = input("access key:")
            secret_access_key = input("secret_access_key:")
            bucket_region = input("s3_bucket_region:")
            #   アクセスキー、シークレットアクセスキー、リージョンを指定し、s3クライアントインスタンスを作成
            s3_client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=bucket_region)
            #   指定したバケットのファイルをダウンロード
            s3_client.download_file(bucket, file, file)
            break
        elif select == "n":
            #   s3クライアントインスタンスを作成
            s3_client = boto3.client("s3")
            #   指定したバケットのファイルをダウンロード
            s3_client.download_file(bucket, file, file)
            break
        else:
            continue
except ClientError as e:
    logging.error(e)
input("続行するには何かキーを押してください...")
