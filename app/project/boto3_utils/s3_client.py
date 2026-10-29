import boto3
from pprint import pprint

import config

s3client = boto3.client(
    service_name='s3',
    region_name=config.AWS_REGION,
    endpoint_url=config.AWS_ENDPOINT_URL_S3,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
)

# CREATE - upload file

target_file_name = 'ivan.html'
s3client.upload_file("Ivan_Yablonskyi.html", "ivan", target_file_name)

# UPDATE
# s3client.upload_file("Audi_A6_2.jpg", config.AWS_BUCKET_NAME, target_file_name)


# READ
public_url = f"{config.AWS_ENDPOINT_URL_S3}/{target_file_name}"
print(public_url)

# list of files
# response = s3client.list_objects_v2(Bucket=config.AWS_BUCKET_NAME)
# pprint(response)

# download
# s3client.download_file(config.AWS_BUCKET_NAME, target_file_name, "555.jpg")

# DELETE
# s3client.delete_object(Bucket=config.AWS_BUCKET_NAME, Key=target_file_name)