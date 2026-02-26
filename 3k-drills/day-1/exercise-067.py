# Day 1 - Exercise 67
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-610', 'mfa_active': True},
    {'username': 'user-226', 'mfa_active': True},
    {'username': 'user-362', 'mfa_active': False},
    {'username': 'user-144', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-362
# user-144
