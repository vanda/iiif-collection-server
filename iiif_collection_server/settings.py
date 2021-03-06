import os
from boto3.session import Session

BUCKET_NAME = os.environ.get('COLLECTION_SERVER_S3_BUCKET')
BASE_FOLDER = os.environ.get('COLLECTION_SERVER_S3_BASE_PREFIX')
ACCESS_KEY = os.environ.get('COLLECTION_SERVER_S3_ACCESS_KEY')
SECRET_KEY = os.environ.get('COLLECTION_SERVER_S3_SECRET_KEY')

