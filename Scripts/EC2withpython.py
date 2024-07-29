import boto3
import time

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')

# Create a security group and allow SSH and HTTP inbound rules
def create_security_group(group_name):
    try:
        security_group = ec2.create_security_group(GroupName=group_name, Description='My security group')
        security_group.authorize_ingress(
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 22,
                    'ToPort': 22,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                },
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 80,
                    'ToPort': 80,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        print(f'Security Group {group_name} created successfully')
        return security_group.id
    except Exception as e:
        print(f'Error creating security group: {e}')
        return None

# Create an EC2 instance
def create_instance(security_group_id):
    try:
        instance = ec2.create_instances(
            ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2 AMI
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='my-key-pair',  # Ensure you have a key pair created and replace with your key pair name
            SecurityGroupIds=[security_group_id],
            UserData='''#!/bin/bash
                        yum update -y
                        yum install -y httpd
                        systemctl start httpd
                        systemctl enable httpd
                        echo "<h1>Welcome to my web server</h1>" > /var/www/html/index.html
                    '''
        )
        instance_id = instance[0].id
        print(f'EC2 Instance {instance_id} created successfully')
        return instance_id
    except Exception as e:
        print(f'Error creating instance: {e}')
        return None

# Main function to set up the environment
def main():
    security_group_name = 'my-security-group'
    security_group_id = create_security_group(security_group_name)
    if security_group_id:
        instance_id = create_instance(security_group_id)
        if instance_id:
            # Wait for the instance to be running
            instance = ec2.Instance(instance_id)
            instance.wait_until_running()
            print(f'Instance {instance_id} is now running')

            # Fetch the public IP address of the instance
            instance.load()
            public_ip = instance.public_ip_address
            print(f'Access your web server at http://{public_ip}')

if __name__ == "__main__":
    main()
