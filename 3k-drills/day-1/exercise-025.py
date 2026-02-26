# Day 1 - Exercise 25
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-164', 'state': 'stopped'},
    {'id': 'i-920', 'state': 'running'},
    {'id': 'i-854', 'state': 'stopped'},
    {'id': 'i-587', 'state': 'stopped'},
    {'id': 'i-148', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-920
