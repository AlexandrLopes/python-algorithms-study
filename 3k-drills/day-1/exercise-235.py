# Day 1 - Exercise 235
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-278', 'mfa_active': True},
    {'username': 'username-463', 'mfa_active': True},
    {'username': 'username-566', 'mfa_active': False},
    {'username': 'username-595', 'mfa_active': False},
    {'username': 'username-890', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

