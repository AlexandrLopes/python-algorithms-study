# Day 1 - Exercise 214
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-523', 'state': 'stopped'},
    {'id': 'i-744', 'state': 'terminated'},
    {'id': 'i-886', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# i-886
