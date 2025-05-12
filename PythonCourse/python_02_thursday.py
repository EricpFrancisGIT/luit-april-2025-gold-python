from helpers import *
from typing import List, Dict, Any


def print_bucket_names(s3_client: Any) -> None:
    """
    Prints the names of all S3 buckets returned by the list_buckets helper function.

    Args:
        s3_client (Any): Boto S3 client object or equivalent.

    """
    bucket_names = List[str]= list_buckets(s3_client)

    for bucket_name in bucket_names: # same as "\n.join(bucket_names)"
        print(bucket_name)
  
def print_instance_ids(ec2_client: Any) -> None:
    """
    Prints the instance IDs from a list of EC2 instances returned by the describe_instances helper function. 

    Args: 
        ec2_client (Any): Boto EC2 client object or equivalent.
    """
    instances = List[Dict[str, Any]] = describe_instances(ec2_client)

    instance_ids = []
    for instance in instances:
        instance_ids.append = (instance['InstanceId'])
             
    for instance_id in instance_ids:
        print(instance_id)


if "__main__" == __name__:
    # Create EC2 and S3 clients
    ec2_client = get_ec2_client()
    s3_client = get_s3_client()

    print_bucket_names(s3_client)
    print_instance_ids(ec2_client)