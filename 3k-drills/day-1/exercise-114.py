# Day 1 - Exercise 114
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-364', 'state': 'stopped'},
    {'id': 'i-397', 'state': 'running'},
    {'id': 'i-484', 'state': 'stopped'},
    {'id': 'i-868', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["state"])


# -----------------------------------
# Expected Output:
# i-397
# i-868
