from helpers import *

def create_instances(ec2_client):
    create_ubuntu_instance(ec2_client)
    print("Create Ubunut")
    create_amazon_linux_2023_instance(ec2_client)
    print("Create Linux 2023")
    create_amazon_linux_2_instance(ec2_client)
    print("Create Linux 2")

ec2_client = get_ec2_client()
create_instances(ec2_client)
