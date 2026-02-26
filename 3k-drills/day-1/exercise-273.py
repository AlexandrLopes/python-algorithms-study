# Day 1 - Exercise 273
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-446', 'mfa_active': False},
    {'username': 'username-704', 'mfa_active': False},
    {'username': 'username-443', 'mfa_active': False},
    {'username': 'username-956', 'mfa_active': False},
    {'username': 'username-550', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

