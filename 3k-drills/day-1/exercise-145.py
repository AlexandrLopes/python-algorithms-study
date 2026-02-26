# Day 1 - Exercise 145
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-787', 'state': 'stopped'},
    {'id': 'i-637', 'state': 'running'},
    {'id': 'i-113', 'state': 'running'},
    {'id': 'i-900', 'state': 'stopped'},
    {'id': 'i-396', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])


# -----------------------------------
# Expected Output:
# i-637
# i-113
