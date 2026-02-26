# Day 1 - Exercise 219
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-426', 'state': 'running'},
    {'id': 'i-305', 'state': 'running'},
    {'id': 'i-267', 'state': 'running'},
    {'id': 'i-873', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# i-426
# i-305
# i-267
