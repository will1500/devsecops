
import boto3
import json

s3 = boto3.client('s3','us-east-2')
ssm = boto3.client('ssm', 'us-east-2')
bucket_name = ssm.get_parameter( Name='baggy765',WithDecryption=False)['Parameter']['Value']
file_name = ssm.get_parameter( Name='dragon_stats_one.txt',WithDecryption=False)['Parameter']['Value']

print(bucket_name)