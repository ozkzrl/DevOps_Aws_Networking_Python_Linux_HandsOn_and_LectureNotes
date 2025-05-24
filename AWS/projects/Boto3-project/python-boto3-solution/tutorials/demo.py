import boto3
import json

# Use Amazon S3
s3 = boto3.client('s3')


# Print out all bucket names
response = s3.list_buckets()

#print(response)
#print(json.dumps(response))
print(json.dumps(response, indent=4, default=str))