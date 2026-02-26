# Day 1 - Exercise 52
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-271', 'mfa_active': True},
    {'username': 'username-336', 'mfa_active': False},
    {'username': 'username-714', 'mfa_active': False},
    {'username': 'username-457', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

