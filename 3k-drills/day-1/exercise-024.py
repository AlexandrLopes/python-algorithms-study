# Day 1 - Exercise 24
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-710', 'state': 'terminated'},
    {'id': 'i-935', 'state': 'terminated'},
    {'id': 'i-378', 'state': 'terminated'},
    {'id': 'i-317', 'state': 'running'},
    {'id': 'i-396', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])


# -----------------------------------
# Expected Output:
# i-317
# i-396
