import boto3
import json
from datetime import datetime 

# Use Amazon EC2
ec2 = boto3.client('ec2')

instances = []
# Describes the specified instances or all instances.
response = ec2.describe_instances(
    Filters=[
        {
        'Name': 'tag-key',
        'Values': ["SchedulerStartTime"]
        }
    ]
)

for reservation in response["Reservations"]:
    instances.extend(reservation["Instances"])


if not instances:
    return_status = "No instances found."
else:
    print(f"Found {len(instances)} instances to process")

    current_hour = f"It's {datetime.now().hour} o'clock now."
    print(current_hour)


    for instance in instances:
        instance_id = instance["InstanceId"]
        message = f"Processing instance {instance_id}"
        print(message)

    return_status = "Finished processing all instances."

print(return_status)


#print(json.dumps(instances, indent=4, default=str))



