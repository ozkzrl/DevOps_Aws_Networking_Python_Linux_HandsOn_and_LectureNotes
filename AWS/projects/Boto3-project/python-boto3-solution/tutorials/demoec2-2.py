import boto3
import json
from datetime import datetime 

def get_instance_tag_value(key, tags):
    for tag in tags:
        if tag['Key'] == key:
            return tag['Value']
    return None


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

    current_hour = datetime.now().hour
    print(f"It's {current_hour } o'clock now.")

    for instance in instances:
        instance_id = instance["InstanceId"]
        instance_state = instance["State"]["Name"]
        instance_tags = instance["Tags"]

        message = f"Processing instance {instance_id}"



        stop_time_tag = get_instance_tag_value("SchedulerStopTime", instance_tags)
        start_time_tag = get_instance_tag_value("SchedulerStartTime", instance_tags)
        print(f"{message} ID: {instance_id}, State: {instance_state}, Tags: {instance_tags}")

        print(f"Stop :{stop_time_tag } Start: {start_time_tag}")



        do_nothing = True

        if instance_state == "running":
            #stop_time_tag = get_instance_tag_value(label_stop_time, instance_tags)
            if stop_time_tag is not None and stop_time_tag.isdigit():
                if int(stop_time_tag) == current_hour:
                    do_nothing = False
                    result = f"Stopping the instance {instance_id}"
                    ec2.stop_instances(InstanceIds=[instance_id])
        
        elif instance_state == "stopped":
            #start_time_tag = get_instance_tag_value(label_start_time, instance_tags)
            if start_time_tag is not None and start_time_tag.isdigit():
                if int(start_time_tag) == current_hour:
                    do_nothing = False
                    result = f"Starting the instance {instance_id}"
                    ec2.start_instances(InstanceIds=[instance_id])
    
        if do_nothing:
            result = f"Instance {instance_id} is in {instance_state}, therefore no action is required."

        print(result)
        
    return_status = "Finished processing all instances."


print(return_status)


#print(json.dumps(instances, indent=4, default=str))



