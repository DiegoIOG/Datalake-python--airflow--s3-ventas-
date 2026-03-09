import boto3
import json
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(data):

    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        region_name=os.getenv("AWS_REGION")
    )

    bucket = os.getenv("S3_BUCKET")

    file_name = f"sales_{data['timestamp']}.json"

    s3.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=json.dumps(data)
    )

    print("Uploaded to S3:", file_name)