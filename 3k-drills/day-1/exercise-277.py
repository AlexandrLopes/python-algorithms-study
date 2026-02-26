# Day 1 - Exercise 277
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-378', 'mfa_active': True},
    {'username': 'username-277', 'mfa_active': True},
    {'username': 'username-302', 'mfa_active': True},
    {'username': 'username-995', 'mfa_active': True},
    {'username': 'username-877', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

