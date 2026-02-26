# Day 1 - Exercise 2
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-257', 'state': 'running'},
    {'id': 'i-926', 'state': 'terminated'},
    {'id': 'i-162', 'state': 'stopped'},
    {'id': 'i-622', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:

for identification in ec2_instances:
    if identification["state"] == "running":
        print(identification["id"])


# -----------------------------------
# Expected Output:
# i-257
