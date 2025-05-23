"""
Required imports:
- boto3 for AWS operations
- json for JSON handling
- datetime for time-based operations
"""
import boto3
import json
from datetime import datetime 

"""
Define the ec2 and s3 boto3 client which we will use as needed.
"""

ec2 = boto3.client("ec2")
s3 = boto3.client("s3")

"""
Define the tag-key values which will determine if the instance needs to be start or stopped. If the instance doesn't have these tags, the scheduler will ignore the instance.
"""

label_start_time = "SchedulerStartTime"
label_stop_time = "SchedulerStopTime"
bucket_prefix = "paulosx"

"""
Return a list of all of the instance that have the key specified.
"""
def get_instances_with_scheduler_tags(list_of_keys):
    
    instances = []

    # Describes the specified instances or all instances.
    response = ec2.describe_instances(
        Filters=[
            {
            'Name': 'tag-key',
            'Values': list_of_keys #["SchedulerStartTime"]
            }
        ]
    )

    for reservation in response["Reservations"]:
        instances.extend(reservation["Instances"])

    return instances

"""
Function to takes a specified key as input and determine the associated value if it exists in the instance tags
"""

def get_tag_value(key, tags):

    for tag in tags:
        if tag['Key'] == key:
            return tag['Value']
    return None

"""
Decide what to do with an instance, given the instance state and current time:
    - if instance is running and stop_time is now, stop it
    - if instance is stopped and start_time is now, start it
    - in all other cases, leave the instance as is
"""

def process_instance(instance, current_hour):

    instance_id = instance["InstanceId"]
    instance_state = instance["State"]["Name"]
    instance_tags = instance["Tags"]

    do_nothing = True

    if instance_state == "running":
        stop_hour = get_tag_value(label_stop_time, instance_tags)
        if stop_hour is not None and stop_hour.isdigit() and int(stop_hour) == current_hour:
            do_nothing = False
            ec2.stop_instances(InstanceIds=[instance_id])
            return f"Stopping the instance {instance_id}"
    
    elif instance_state == "stopped":
        start_hour = get_tag_value(label_start_time, instance_tags)
        if start_hour is not None and start_hour.isdigit() and int(start_hour) == current_hour:
            do_nothing = False
            ec2.start_instances(InstanceIds=[instance_id])
            return f"Starting the instance {instance_id}"
    
    if do_nothing:
        result = f"Instance {instance_id} is in {instance_state}, therefore no action is required."

    return result

"""
Get the list of all instances that have the start and stop tags,
the process those instances
"""

def handle_ec2_instances():
    
    instances = get_instances_with_scheduler_tags([label_start_time])
    if not instances:
        return_status = "No instances found with scheduler tags."
    else:
        print(f"Found {len(instances)} instances to process")
        
        current_hour = datetime.now().hour
        print(f"It's {current_hour } o'clock now.")

        for instance in instances:
            message = process_instance(instance, current_hour)
            print(message)
        
        return_status = "Finished processing all instances."

    return return_status

"""
Check the versioning is enabled on the specified bucket. If not, then enable versioning.
"""
def ensure_versioning(bucket_name):

    response = s3.get_bucket_versioning(Bucket=bucket_name)

    if response.get("Status") != "Enabled":
        s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={"Status": "Enabled"}
        )
        result = f"Enabled versioning on bucket {bucket_name}"
    else:
        result = f"Versioning already enabled on bucket {bucket_name}"       

    return result

"""
Get the list of all buckets and process each one
"""

def handle_s3_buckets():
    
    response = s3.list_buckets()
    buckets = response["Buckets"]
    
    if not buckets:
        return_status = "No buckets found."
    else:
        print(f"Found {len(buckets)} buckets to process.")

        for bucket in buckets:
            bucket_name = bucket["Name"]

            # do this to prevent modifying other buckets which are not part of this test.
            if bucket_name.startswith(bucket_prefix):
                result = ensure_versioning(bucket_name)
            else:
                result = f"Skipping the bucket {bucket_name}"

            print(result)

        return_status = "Finished processing all bucket"
    
    return return_status


def lambda_handler(event, context):
    try:
        ec2_result = handle_ec2_instances()
        s3_result = handle_s3_buckets()
        status_message = f"EC2 Result:\n{ec2_result}\n\nS3 Result:\n{s3_result}"
        status_code = 200
    except Exception as e:
        status_message = f"Unexpected error occurred: {str(e)}"
        status_code = 500
    finally:
        print(status_message)
        return {
            "statusCode": status_code,
            "body": json.dumps(status_message)
        }

if __name__ == "__main__":
    lambda_handler(None, None)