import boto3
import json
from datetime import datetime

BUCKET_NAME = "crypto-pipeline-gui"

def save_to_s3(data, prefix):
    s3 = boto3.client("s3")

    timestamp = datetime.now().strftime("%HH-%MM-%SS")
    key = f"{prefix}/Year={datetime.now().year}/Month={datetime.now().month}/Day={datetime.now().day}/crypto_{timestamp}.json"

    json_data = json.dumps(data)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json_data,
        ContentType="application/json"
    )

