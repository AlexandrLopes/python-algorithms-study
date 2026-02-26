# Day 1 - Exercise 108
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-598', 'state': 'terminated'},
    {'id': 'i-284', 'state': 'terminated'},
    {'id': 'i-451', 'state': 'running'},
    {'id': 'i-640', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-451
