# Day 1 - Exercise 103
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-287', 'mfa_active': True},
    {'username': 'username-755', 'mfa_active': True},
    {'username': 'username-782', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

