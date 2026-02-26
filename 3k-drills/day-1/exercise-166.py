# Day 1 - Exercise 166
# Context: Cloud Auditing. Find all EC2 instances that are currently 'running'.

ec2_instances = [
    {'id': 'i-230', 'state': 'running'},
    {'id': 'i-735', 'state': 'stopped'},
    {'id': 'i-197', 'state': 'running'},
    {'id': 'i-909', 'state': 'running'},
    {'id': 'i-959', 'state': 'running'}
]

# TODO: Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'.
# Write your code below:
for i in ec2_instances:
    if i["state"] == "running":
        print(i["id"])



# -----------------------------------
# Expected Output:
# i-230
# i-197
# i-909
# i-959
