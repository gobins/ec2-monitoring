import boto3
import pprint

ec2 = boto3.resource('ec2')

for vpc in ec2.vpcs.all():
    for subnet in vpc.subnets.all():
    	response = ec2.meta.client.describe_instances(Filters=[{'Name': 'subnet-id', 'Values': [ subnet.id ]}])
    	reservations = response['Reservations']
    	if(reservations):
          list_instances = reservations[0]
          print(list_instances)