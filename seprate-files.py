import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        file_extension = os.path.splitext(object_key)[-1].lower()

        if file_extension == '.pdf':
            destination_bucket = 'pdf-output-bucket121'
        elif file_extension == '.txt':
            destination_bucket = 'txt-output-bucket'
        elif file_extension == '.jpeg' or file_extension == '.jpg':
            destination_bucket = 'jpeg-output-bucket'
        else:
            # Handle unsupported file types or log the event
            continue

        s3_client.copy_object(
            Bucket=destination_bucket,
            CopySource={'Bucket': bucket_name, 'Key': object_key},
            Key=object_key
        )
