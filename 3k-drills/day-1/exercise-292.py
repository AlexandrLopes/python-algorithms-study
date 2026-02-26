# Day 1 - Exercise 292
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-528', 'state': 'running'},
    {'id': 'i-485', 'state': 'stopped'},
    {'id': 'i-980', 'state': 'stopped'},
    {'id': 'i-568', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:



# -----------------------------------
# Expected Output:
# i-528
# i-568
