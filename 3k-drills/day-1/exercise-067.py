# Day 1 - Exercise 67
# Context: Cloud Auditing. You need to find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'id-303', 'state': 'terminated'},
    {'id': 'id-453', 'state': 'stopped'},
    {'id': 'id-827', 'state': 'stopped'},
    {'id': 'id-101', 'state': 'running'},
    {'id': 'id-883', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:

