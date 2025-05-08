import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-095c0aca9561d26b0').terminate() # put your instance id