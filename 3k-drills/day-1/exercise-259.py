# Day 1 - Exercise 259
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-688', 'state': 'stopped'},
    {'id': 'i-324', 'state': 'running'},
    {'id': 'i-614', 'state': 'stopped'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# i-324
