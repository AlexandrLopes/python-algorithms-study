# Day 1 - Exercise 19
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-355', 'state': 'running'},
    {'id': 'i-349', 'state': 'running'},
    {'id': 'i-849', 'state': 'terminated'},
    {'id': 'i-997', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-355
# i-349
# i-997
