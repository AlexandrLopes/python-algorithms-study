# Day 1 - Exercise 157
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-784', 'state': 'running'},
    {'id': 'i-877', 'state': 'running'},
    {'id': 'i-355', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-784
# i-877
