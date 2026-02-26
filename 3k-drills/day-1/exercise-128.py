# Day 1 - Exercise 128
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-776', 'mfa_active': False},
    {'username': 'username-398', 'mfa_active': False},
    {'username': 'username-602', 'mfa_active': True},
    {'username': 'username-796', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

