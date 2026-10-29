import os
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_USERNAME = os.environ.get('REDIS_USERNAME')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')


AWS_ENDPOINT_URL_S3="https://br-tiny-star-b40ki5an.storage.c-6.us-east-2.aws.neon.tech"
AWS_ACCESS_KEY_ID="nak_live_fb44fa0f06d444a987b5a19470ea92a0"
AWS_SECRET_ACCESS_KEY="nsk_live_fb22d9deea2007f81f539ea9124746612271305b3ef24e33e09be432ad9c3630"
AWS_REGION="us-east-2"