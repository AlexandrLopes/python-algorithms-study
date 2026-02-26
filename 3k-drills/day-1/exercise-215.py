# Day 1 - Exercise 215
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-538', 'mfa_active': True},
    {'username': 'username-453', 'mfa_active': True},
    {'username': 'username-441', 'mfa_active': True},
    {'username': 'username-279', 'mfa_active': True},
    {'username': 'username-828', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

