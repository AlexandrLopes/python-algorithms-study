# Day 1 - Exercise 65
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-380', 'state': 'terminated'},
    {'id': 'i-219', 'state': 'running'},
    {'id': 'i-413', 'state': 'running'},
    {'id': 'i-122', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])


# -----------------------------------
# Expected Output:
# i-219
# i-413
# i-122
