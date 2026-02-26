# Day 1 - Exercise 124
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-855', 'state': 'stopped'},
    {'id': 'i-189', 'state': 'stopped'},
    {'id': 'i-231', 'state': 'running'},
    {'id': 'i-501', 'state': 'terminated'},
    {'id': 'i-547', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-231
