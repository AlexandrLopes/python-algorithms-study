# Day 1 - Exercise 77
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-902', 'state': 'running'},
    {'id': 'i-897', 'state': 'terminated'},
    {'id': 'i-683', 'state': 'terminated'},
    {'id': 'i-360', 'state': 'terminated'},
    {'id': 'i-765', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-902
# i-765
