import logging
import boto3
from botocore.exceptions import ClientError
import os

def func_download_files(download_bucket_name: str, target_prefix: str) -> None:
    """aws s3の指定したバケット内の、指定したプレフィックスを持つファイルを全てダウンロードする。"""
    s3_client = boto3.client("s3")
#   指定したバケット内の、指定したプレフィックスを持つファイルのリストを取得する。
    response = s3_client.list_objects(Bucket=download_bucket_name, Prefix=target_prefix)
    download_list = [object_data["Key"] for object_data in response["Contents"]]
    
#   ファイルのダウンロード処理
    for download_key in download_list:
#   ディレクトリの場合、何も実行せず次の繰り返し処理に移る。
        if download_key[-1] == "/":
            continue
        download_file_name = os.path.basename(download_key)
#   指定したプレフィックスを持つファイルをダウンロード
        s3_client.download_file(Bucket=download_bucket_name, Key=download_key, Filename=download_file_name)



#   バケット名、プレフィックス、ダウンロード先のパスを入力
bucket_name = input("bucket name:")
prefix = input("folder(prefix):")
path = input("Download path:")

#   カレントディレクトリを、ダウンロード先ディレクトリに移動
os.chdir(path)

#   s3バケットから、指定したプレフィックスのファイルをダウンロード
func_download_files(bucket_name, prefix)

#   何かキーを入力するまで実行画面を表示
input("続行するには何かキーを押してください...")
