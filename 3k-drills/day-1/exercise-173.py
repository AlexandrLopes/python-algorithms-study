# Day 1 - Exercise 173
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-105', 'mfa_active': False},
    {'username': 'username-511', 'mfa_active': True},
    {'username': 'username-182', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

