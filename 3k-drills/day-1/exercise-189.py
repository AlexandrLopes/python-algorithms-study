# Day 1 - Exercise 189
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-979', 'mfa_active': True},
    {'username': 'username-292', 'mfa_active': True},
    {'username': 'username-668', 'mfa_active': False},
    {'username': 'username-838', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

