# Day 1 - Exercise 196
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-498', 'state': 'terminated'},
    {'id': 'i-535', 'state': 'terminated'},
    {'id': 'i-690', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
