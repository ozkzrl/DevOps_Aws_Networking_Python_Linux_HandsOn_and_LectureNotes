import json
import boto3

# Use Amazon S3
s3 = boto3.client('s3')

bucket_name='paul-demo1234567'

#Returns the versioning state of a bucket
response = s3.get_bucket_versioning(Bucket=bucket_name)




is_enabled = response.get("Status", "Disabled")

if is_enabled == "Enabled":
    result = f"Versioning is enabled on bucket {bucket_name}"
else:
    versioning_configuration = {"Status": "Enabled"}
    
    # Sets a bucket's versioning state: "Enabled" or "Suspended"
    s3.put_bucket_versioning(Bucket=bucket_name,VersioningConfiguration=versioning_configuration)
    
    result = f"Enabling versioning on bucket {bucket_name}"

print(result)
# #print(json.dumps(result, indent=4, default=str))
# #print(json.dumps(response.get("Status"), indent=4, default=str))
# #print(response)


#print(response)  
#print(json.dumps(is_enabled, indent=4, default=str))
