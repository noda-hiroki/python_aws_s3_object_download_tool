import logging
import boto3
from botocore.exceptions import ClientError
import os

#   バケット名、ファイル名、ダウンロード先のパスを入力
bucket = input("bucket name:")
file = input("file name:")
path = input("Download path:")
#   s3クライアントインスタンスを作成
s3_client = boto3.client("s3")
#   カレントディレクトリを、ダウンロード先ディレクトリに移動
os.chdir(path)

try:
#   指定したバケットのファイルをダウンロード
    s3_client.download_file(bucket, file, file)
except ClientError as e:
    logging.error(e)
# os.system("PAUSE")
input("続行するには何かキーを押してください...")
