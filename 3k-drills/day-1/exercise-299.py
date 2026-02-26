# Day 1 - Exercise 299
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-552', 'mfa_active': False},
    {'username': 'user-711', 'mfa_active': True},
    {'username': 'user-290', 'mfa_active': True},
    {'username': 'user-374', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-552
# user-374
