import boto3
import json
import pprint

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
reservations = response['Reservations']
list_instances = reservations[0]

pprint.pprint(list_instances)
for instance in list_instances['Instances']:
  
  instance_data = {}
  instance_data['ImageId'] = instance['ImageId']
  instance_data['InstanceId'] = instance['InstanceId']
  instance_data['InstanceType'] = instance['InstanceType']
  instance_data['LaunchTime'] = instance['LaunchTime']
  instance_data['State'] = instance['State']
  instance_data['PrivateIpAddress'] = instance['PrivateIpAddress']
  instance_data['SubnetId'] = instance['SubnetId']
  instance_data['Tags'] = instance['Tags']


  pprint.pprint(instance_data)

# ec2 = boto3.resource('ec2')
# instances = ec2.instances.filter(
#     Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
# for instance in instances:
#     print(instance.id, instance.instance_type)





