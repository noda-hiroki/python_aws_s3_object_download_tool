import logging
import boto3
from botocore.exceptions import ClientError
import os

def func_download_files(download_bucket_name: str, target_prefix: str) -> None:
    """aws s3の指定したバケット内の、指定したプレフィックスを持つファイルを全てダウンロードする。"""
    try:
        while True:
            select = input("Select whether to set an access key, secret access key, and region.(y/n):")
            if select == "y":
                #   アクセスキー、シークレットアクセスキー、リージョンを設定
                access_key = input("access key:")
                secret_access_key = input("secret_access_key:")
                bucket_region = input("s3_bucket_region(Example[Tokyo]: ap-northeast-1):")
                #   アクセスキー、シークレットアクセスキー、リージョンを指定し、s3クライアントインスタンスを作成
                s3_client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=bucket_region)
            elif select == "n":
                s3_client = boto3.client("s3")
            else:
                continue
            #   指定したバケット内の、指定したプレフィックスを持つファイルのリストを取得する。
            response = s3_client.list_objects(Bucket=download_bucket_name, Prefix=target_prefix)
            download_list = [object_data["Key"] for object_data in response["Contents"]]
            
            #   ファイルのダウンロード処理
            for download_key in download_list:
                #   ディレクトリの場合、何も実行せず次の繰り返し処理に移る。
                if download_key[-1] == "/":
                    continue
                download_file_name = os.path.basename(download_key)
                #   ファイルをダウンロード
                s3_client.download_file(Bucket=download_bucket_name, Key=download_key, Filename=download_file_name)
            break
    except ClientError as e:
        logging.error(e)
        return False
    return True



try:
    while True:
        #   条件分岐：プレフィックスを指定し、配下のファイルを全てダウンロードするか？
        select_1 = input("Specify a prefix and download all files under it?(y/n)")
        if select_1 == "y":
            #   バケット名、プレフィックス、ダウンロード先のパスを入力
            bucket = input("bucket name:")
            prefix = input("prefix in s3 bucket(Example: log/security):")
            path = input("Download path:")
            #   カレントディレクトリを、ダウンロード先ディレクトリに移動
            os.chdir(path)
            #   aws s3の指定したバケット内の、指定したプレフィックスを持つファイルを全てダウンロード
            func_download_files(bucket, prefix)
        elif select_1 == "n":
            #   バケット名、ファイル名、ダウンロード先のパスを入力
            bucket = input("bucket name:")
            file = input("Key of file in s3 bucket(Example: text/test.txt):")
            path = input("Download path:")
            #   カレントディレクトリを、ダウンロード先ディレクトリに移動
            os.chdir(path)
            while True:
                select_2 = input("Select whether to set an access key, secret access key, and region.(y/n):")
                if select_2 == "y":
                    #   アクセスキー、シークレットアクセスキー、リージョンを設定
                    access_key = input("access key:")
                    secret_access_key = input("secret_access_key:")
                    bucket_region = input("s3_bucket_region(Example[Tokyo]: ap-northeast-1):")
                    #   アクセスキー、シークレットアクセスキー、リージョンを指定し、s3クライアントインスタンスを作成
                    s3_client = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_access_key, region_name=bucket_region)
                elif select_2 == "n":
                    #   s3クライアントインスタンスを作成
                    s3_client = boto3.client("s3")
                else:
                    continue
                #   ファイルをダウンロード
                file_name = os.path.basename(file)
                s3_client.download_file(bucket, file, file_name)
                break
        else:
            continue
        break
except ClientError as e:
    logging.error(e)
input("続行するには何かキーを押してください...")
