# Day 1 - Exercise 236
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-429', 'state': 'running'},
    {'id': 'i-507', 'state': 'terminated'},
    {'id': 'i-332', 'state': 'running'},
    {'id': 'i-372', 'state': 'terminated'},
    {'id': 'i-393', 'state': 'terminated'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-429
# i-332
