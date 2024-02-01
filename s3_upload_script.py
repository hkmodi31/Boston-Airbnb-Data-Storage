import boto3
import pandas as pd
import os
import aws_config

s3 = boto3.resource(
    service_name="s3",
    region_name="us-east-1",
    aws_access_key_id = aws_config.aws_access_key_id,
    aws_secret_access_key = aws_config.aws_secret_access_key,
)

for file in os.listdir("./processed_csv_files"):
    s3.Bucket('boston-airbnb').upload_file(Filename=f"./processed_csv_files/{file}", Key=file)