# Day 1 - Exercise 151
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-295', 'mfa_active': True},
    {'username': 'username-758', 'mfa_active': True},
    {'username': 'username-975', 'mfa_active': True},
    {'username': 'username-951', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

