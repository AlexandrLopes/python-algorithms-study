# Day 1 - Exercise 206
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-517', 'state': 'stopped'},
    {'id': 'i-866', 'state': 'terminated'},
    {'id': 'i-838', 'state': 'running'},
    {'id': 'i-803', 'state': 'stopped'},
    {'id': 'i-469', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-838
# i-469
