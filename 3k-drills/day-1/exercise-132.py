# Day 1 - Exercise 132
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-247', 'state': 'running'},
    {'id': 'i-978', 'state': 'stopped'},
    {'id': 'i-843', 'state': 'running'},
    {'id': 'i-951', 'state': 'running'},
    {'id': 'i-798', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])

# -----------------------------------
# Expected Output:
# i-247
# i-843
# i-951
