# Day 1 - Exercise 40
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-853', 'state': 'running'},
    {'id': 'i-591', 'state': 'running'},
    {'id': 'i-547', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for name in ec2_instances:
    if name["state"] == "running":
        print(name["id"])


# -----------------------------------
# Expected Output:
# i-853
# i-591
# i-547
