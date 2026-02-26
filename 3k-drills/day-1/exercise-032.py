# Day 1 - Exercise 32
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-470', 'mfa_active': False},
    {'username': 'username-443', 'mfa_active': True},
    {'username': 'username-703', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

