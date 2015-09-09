import boto3
import pprint

ec2 = boto3.resource('ec2')

for vpc in ec2.vpcs.all():
    for subnet in vpc.subnets.all():
    	print("List of instances in subnet: " + subnet.cidr_block)
    	for instance in subnet.instances.all():
    		print(instance.id)
