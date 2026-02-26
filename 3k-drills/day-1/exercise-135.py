# Day 1 - Exercise 135
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-868', 'mfa_active': True},
    {'username': 'username-279', 'mfa_active': False},
    {'username': 'username-430', 'mfa_active': False},
    {'username': 'username-712', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

