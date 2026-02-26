# Day 1 - Exercise 277
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-238', 'mfa_active': True},
    {'username': 'user-808', 'mfa_active': True},
    {'username': 'user-554', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-554
