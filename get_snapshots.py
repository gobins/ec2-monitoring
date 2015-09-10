import boto3
import pprint

client = boto3.client('ec2')

ec2 = boto3.resource("ec2")

pprint.pprint(ec2.meta.client.describe_snapshots(SnapshotIds=['snap-a8d13d40']))
print(ec2.Snapshot('snap-a8d13d40'))
# snapshots = ec2.snapshots.all()

# print(dir(snapshots))

# for snapshot in snapshots:
# 	print snapshot

# snapshots = client.describe_snapshots()

# print(len(snapshots['Snapshots']))