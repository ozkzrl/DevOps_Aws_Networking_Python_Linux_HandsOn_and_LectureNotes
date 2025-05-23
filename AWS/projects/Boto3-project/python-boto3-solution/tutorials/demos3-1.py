import json
import boto3

# Use Amazon S3
s3 = boto3.client('s3')

prefix = "paulo"

# Print out all bucket names
response = s3.list_buckets()
bucket_list = response["Buckets"]


if len(bucket_list) == 0:
    return_status = "No buckets found."
else:
    print(f"Found {len(bucket_list)} buckets to process.")
    for bucket in bucket_list:
        bucket_name = bucket["Name"]
        #print(f" {bucket_name}")

         # do this to prevent modifying other buckets which are not part of this test.
        if bucket_name.startswith(prefix):
            message = f"Processing the bucket {bucket_name}"
        else:
            message = f"Skipping the bucket {bucket_name}"
        print(message)
    
    return_status = "Finished processing all bucket"



print(return_status)
#print(json.dumps(bucket_list, indent=4, default=str))
#print(bucket_list)