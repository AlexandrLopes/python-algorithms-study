# Day 3 - Exercise 13 | ID: 135
# Theme: Exception Handling (KeyError)
# Context: Tagging Audit. Some EC2 instances are missing the 'Tags' key entirely.

instances = [
    {'id': 'i-01', 'Tags': {'Env': 'Prod'}},
    {'id': 'i-02'},
    {'id': 'i-03', 'Tags': {'Env': 'Dev'}}
]

# TODO: Loop through the instances. Use try/except. Print the 'Env' tag. If KeyError occurs, print 'Untagged'.
# Write your code below:



# -----------------------------------
# Expected Output:
# Prod
# Untagged
# Dev
