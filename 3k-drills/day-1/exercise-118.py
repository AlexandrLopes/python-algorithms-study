# Day 1 - Exercise 118
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-883', 'state': 'terminated'},
    {'id': 'i-966', 'state': 'running'},
    {'id': 'i-896', 'state': 'stopped'},
    {'id': 'i-892', 'state': 'stopped'},
    {'id': 'i-294', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-966
# i-294
