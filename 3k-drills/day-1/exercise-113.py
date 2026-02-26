# Day 1 - Exercise 113
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-605', 'state': 'terminated'},
    {'id': 'i-414', 'state': 'running'},
    {'id': 'i-699', 'state': 'stopped'},
    {'id': 'i-113', 'state': 'stopped'},
    {'id': 'i-793', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-414
# i-793
