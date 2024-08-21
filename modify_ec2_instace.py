import boto3

instance_id = 'i-0d024e2800c243a1b'
new_intance_type = 't2.nano'

ec2_client = boto3.client('ec2')

try:
    response = ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        InstanceType={
            'Value': new_intance_type
        }
    )

    print(f"Instance {instance_id} has been modified to {new_intance_type}")
except Exception as e:
    print(f"Error: {e}")