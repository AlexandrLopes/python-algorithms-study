# Day 1 - Exercise 289
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-376', 'mfa_active': True},
    {'username': 'username-130', 'mfa_active': True},
    {'username': 'username-948', 'mfa_active': True},
    {'username': 'username-542', 'mfa_active': False},
    {'username': 'username-740', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

