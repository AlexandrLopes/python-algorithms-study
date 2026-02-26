# Day 1 - Exercise 106
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-589', 'state': 'stopped'},
    {'id': 'i-340', 'state': 'running'},
    {'id': 'i-932', 'state': 'stopped'},
    {'id': 'i-530', 'state': 'terminated'},
    {'id': 'i-738', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-340
