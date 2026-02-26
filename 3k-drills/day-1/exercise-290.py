# Day 1 - Exercise 290
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-694', 'state': 'terminated'},
    {'id': 'i-605', 'state': 'stopped'},
    {'id': 'i-420', 'state': 'running'},
    {'id': 'i-660', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# i-420
