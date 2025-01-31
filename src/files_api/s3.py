import boto3
from mypy_boto3_s3 import S3Client
from mypy_boto3_s3.type_defs import PutObjectOutputTypeDef

BUCKET_NAME = 'mlops-cloud-nk'

session = boto3.Session()
s3_client: S3Client = boto3.client('s3')



#write a file to s3 bucket with hello world"

s3_client.put_object(Bucket=BUCKET_NAME, Key='folder1/hello.txt', Body="hello world!", ContentType='text/plain')

print(f'File has been written to S3 bucket {BUCKET_NAME}')  
    
    