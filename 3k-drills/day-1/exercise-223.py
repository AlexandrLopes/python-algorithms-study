# Day 1 - Exercise 223
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-643', 'mfa_active': True},
    {'username': 'user-744', 'mfa_active': True},
    {'username': 'user-926', 'mfa_active': False},
    {'username': 'user-799', 'mfa_active': False},
    {'username': 'user-110', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-926
# user-799
