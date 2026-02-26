# Day 1 - Exercise 63
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-216', 'mfa_active': True},
    {'username': 'username-672', 'mfa_active': True},
    {'username': 'username-558', 'mfa_active': False},
    {'username': 'username-239', 'mfa_active': True},
    {'username': 'username-602', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

