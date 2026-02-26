# Day 1 - Exercise 57
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-150', 'state': 'stopped'},
    {'id': 'i-693', 'state': 'terminated'},
    {'id': 'i-522', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-522
