# Day 1 - Exercise 271
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-477', 'state': 'terminated'},
    {'id': 'i-776', 'state': 'running'},
    {'id': 'i-467', 'state': 'stopped'},
    {'id': 'i-758', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-776
