# Overview

This Python script automates the monitoring of AWS EC2 instances. It checks the state of all instances in a specified AWS region and restarts any stopped instances automatically. This ensures high availability and reduces manual intervention.

# Features

* Retrieves all EC2 instances in a given AWS region.

* Identifies stopped instances.

* Restarts stopped instances automatically.

* Provides logs/notifications for restarted instances.
  
# Prerequisites

Before running this script, ensure you have:

1. Python 3.x installed.

2. Boto3 installed (AWS SDK for Python):
```
    pip install boto3
```
3. AWS CLI configured with appropriate credentials:
```
    aws configure
```
# Installation & Usage

# Example Output
1. Clone or download this repository.

2. Modify the AWS region in the script if needed:
```
    AWS_REGION = "us-east-1"  # Change to your AWS region
```
3. Run the script:
```
    python ec2_health_check.py
```

```
    🔄 Restarting 2 stopped instances...
    ✅ Instance i-1234567890abcdef0 restarted successfully.
    ✅ Instance i-0987654321abcdef1 restarted successfully.
```
If all instances are running:
```
    ✅ All instances are running.
```
# Customization

* Modify the script to monitor specific EC2 instances instead of all.

* Add email or Slack notifications after restarting an instance.

* Extend it to monitor other AWS resources like RDS, Lambda, etc.

# License

This project is open-source and available under the MIT License.

