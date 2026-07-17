import os
import boto3
from dotenv import load_dotenv

load_dotenv()


class AWSUploader:

    def __init__(self):

        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )

        self.bucket = os.getenv("S3_BUCKET")

    def connect_aws(self, **context):

        local_file = context["ti"].xcom_pull(
            task_ids="extract_weather_data"
        )

        filename = os.path.basename(local_file)

        self.s3.upload_file(
            local_file,
            self.bucket,
            f"bronze/{filename}"
        )

        print("Uploaded Successfully")