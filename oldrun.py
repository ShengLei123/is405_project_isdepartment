import boto3
import paramiko
import time
import socket

socket.getaddrinfo('127.0.0.1', 8080)

def ssh_connect_with_retry(ssh, ip_address, retries):
    if retries > 3:
        return False
    privkey = paramiko.RSAKey.from_private_key_file(
        'E:/IS405\ISDepartment/Project-1-keypayr.pem')
    interval = 5
    try:
        retries += 1
        print('SSH into the instance: {}'.format(ip_address))
        
        ssh.connect(hostname=ip_address, 
                    username='ec2-user', pkey=privkey)
        return True
    except Exception as e:
        print(e)
        time.sleep(interval)
        print('Retrying SSH connection to {}'.format(ip_address))
        ssh_connect_with_retry(ssh, ip_address, retries)

# get your instance ID from AWS dashboard

# get instance
# ec2 = boto3.resource('ec2', region_name='us-east-2')
# instance = ec2.Instance(id='i-0c9ff70ecf12573ac')
# # instance.wait_until_running()
# current_instance = list(ec2.instances.filter(InstanceIds=['i-0c9ff70ecf12573ac']))
# ip_address = current_instance[0].public_ip_address

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_connect_with_retry(ssh, 'ec2-user@ec2-18-222-126-225.us-east-2.compute.amazonaws.com', 0)

stdin, stdout, stderr = ssh.exec_command(commands)
print('stdout:', stdout.read())
print('stderr:', stderr.read())