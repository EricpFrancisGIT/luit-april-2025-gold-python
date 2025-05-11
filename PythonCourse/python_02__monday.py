from helpers import *

def create_instances(ec2_client, ami_type="Ubuntu", instance_amount=1):
    for i in range(instance_amount)
        if ami_type.lower().strip() == "Ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Create Ubuntu")
        elif ami_type.lower().strip() == "Linux 2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Create Linux 2023")
        elif ami_type.lower().strip() == "Linux 2":
            create_amazon_linux_2_instance(ec2_client)
            print("Create Linux 2")
        else:
            print("Invalid AMI type. Please choose 'Ubuntu', 'Linux 2023', or 'Linux 2'.")
            break
#     create_instance(client, "ami-0c55b159cbfafe1f0")  # Call create_instance with the Amazon Linux 2 AMI ID

if "__main__" == __name__:
    ec2_client = get_ec2_client()
    create_instances(ec2_client)
    create_instances(ec2_client, ami_type="Linux 2023")
    create_instances(ec2_client, ami_type="Linux 2")
    create_instances(ec2_client, ami_type="Windows 11")
    create_instances(ec2_client, ami_type="Ubuntu", instance_amount=3)
    