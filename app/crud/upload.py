import boto3
import logging
import uuid
from botocore.exceptions import ClientError

client = boto3.client("s3")

bucket = "stunning-s3-bucket"


def upload_file(filename: str):
    filename = filename
    key = str(uuid.uuid4())

    try:
        client.upload_file(filename, bucket, key)
    except ClientError as e:
        logging.error(e)
        return False

    location = boto3.client("s3").get_bucket_location(Bucket=bucket)[
        "LocationConstraint"
    ]
    url = f"https://{bucket}.s3.{location}.amazonaws.com/{key}"
    return url


def download_file(filename: str, file_uuid: str):
    filename = filename
    key = file_uuid

    try:
        client.download_file(bucket, key, filename)
    except ClientError as e:
        logging.error(e)
        return False
