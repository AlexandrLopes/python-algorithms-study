# Day 1 - Exercise 107
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-560', 'state': 'running'},
    {'id': 'i-302', 'state': 'terminated'},
    {'id': 'i-558', 'state': 'running'},
    {'id': 'i-264', 'state': 'terminated'},
    {'id': 'i-100', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-560
# i-558
