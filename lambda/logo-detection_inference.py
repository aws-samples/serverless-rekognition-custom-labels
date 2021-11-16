import json
import boto3
from urllib.parse import unquote_plus

rekognition = boto3.client('rekognition')
model = 'PROJECT-VERSION-ARN' # put here your trained model ARN
min_confidence = 50 # minimum confidence percentage of the requested inference

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    for message in event['Records']:
        records = json.loads(message['body'])['Records']
        for record in records:

            bucket = record['s3']['bucket']['name']
            key = unquote_plus(record['s3']['object']['key'])

            #Call DetectCustomLabels
            response = rekognition.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': key}},
                MinConfidence=min_confidence,
                ProjectVersionArn=model)
                
            destination_key = key + '.json'
            destination_path = '/tmp/response.json'
            
            with open(destination_path, 'w') as fp:
                json.dump(response, fp)
            
            s3.upload_file(destination_path, bucket, destination_key)
            
    
    event['status'] = 'COMPLETED'
    return event
