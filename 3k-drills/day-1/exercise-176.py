# Day 1 - Exercise 176
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-395', 'state': 'terminated'},
    {'id': 'i-575', 'state': 'terminated'},
    {'id': 'i-614', 'state': 'terminated'},
    {'id': 'i-156', 'state': 'running'},
    {'id': 'i-375', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-156
