# Day 1 - Exercise 66
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-546', 'state': 'stopped'},
    {'id': 'i-832', 'state': 'running'},
    {'id': 'i-553', 'state': 'running'},
    {'id': 'i-481', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "runnning":
        print(i["id"])


# -----------------------------------
# Expected Output:
# i-832
# i-553
# i-481
