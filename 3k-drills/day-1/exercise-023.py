# Day 1 - Exercise 23
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-397', 'mfa_active': False},
    {'username': 'username-648', 'mfa_active': True},
    {'username': 'username-868', 'mfa_active': True},
    {'username': 'username-630', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

