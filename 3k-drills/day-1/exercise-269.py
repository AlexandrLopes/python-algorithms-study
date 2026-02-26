# Day 1 - Exercise 269
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-628', 'state': 'terminated'},
    {'id': 'i-678', 'state': 'stopped'},
    {'id': 'i-140', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
