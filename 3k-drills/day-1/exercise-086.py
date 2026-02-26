# Day 1 - Exercise 86
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-319', 'mfa_active': True},
    {'username': 'user-242', 'mfa_active': True},
    {'username': 'user-105', 'mfa_active': False},
    {'username': 'user-519', 'mfa_active': False},
    {'username': 'user-925', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-105
# user-519
# user-925
