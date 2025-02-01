import boto3

# AWS Configuration
AWS_REGION = "us-east-1"  # Change to your AWS region

# Initialize EC2 Client
ec2_client = boto3.client("ec2", region_name=AWS_REGION)

def get_instances():
    """Retrieve all EC2 instances."""
    response = ec2_client.describe_instances()
    instances = []
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "InstanceId": instance["InstanceId"],
                "State": instance["State"]["Name"]
            })
    
    return instances

def restart_stopped_instances():
    """Check and restart stopped EC2 instances."""
    instances = get_instances()
    
    stopped_instances = [inst["InstanceId"] for inst in instances if inst["State"] == "stopped"]
    
    if not stopped_instances:
        print("✅ All instances are running.")
        return
    
    print(f"🔄 Restarting {len(stopped_instances)} stopped instances...")
    ec2_client.start_instances(InstanceIds=stopped_instances)
    
    for instance_id in stopped_instances:
        print(f"✅ Instance {instance_id} restarted successfully.")

if __name__ == "__main__":
    restart_stopped_instances()
