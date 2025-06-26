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


            bucket_versioning=s3.get_bucket_versioning(Bucket=bucket_name)
            print(json.dumps(bucket_versioning, indent=4, default=str))

            is_enabled = bucket_versioning.get("Status", "Disabled")
            
            if is_enabled == "Enabled":
                result = f"Versioning is enabled on bucket {bucket_name}"
            else:
                versioning_configuration = {"Status": "Enabled"}
                s3.put_bucket_versioning(Bucket=bucket_name,VersioningConfiguration=versioning_configuration)
                result = f"Enabling versioning on bucket {bucket_name}"
            print(result)

        else:
            message = f"Skipping the bucket {bucket_name}"
        print(message)
        
    
    return_status = "Finished processing all bucket"

print(return_status)
#print(json.dumps(bucket_list, indent=4, default=str))
#print(bucket_list)