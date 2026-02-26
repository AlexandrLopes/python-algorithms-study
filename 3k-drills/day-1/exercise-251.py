# Day 1 - Exercise 251
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-569', 'state': 'stopped'},
    {'id': 'i-443', 'state': 'terminated'},
    {'id': 'i-661', 'state': 'stopped'},
    {'id': 'i-266', 'state': 'running'},
    {'id': 'i-472', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-266
# i-472
