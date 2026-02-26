# Day 1 - Exercise 32
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-684', 'state': 'stopped'},
    {'id': 'i-407', 'state': 'stopped'},
    {'id': 'i-981', 'state': 'running'},
    {'id': 'i-436', 'state': 'terminated'},
    {'id': 'i-124', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-981
# i-124
