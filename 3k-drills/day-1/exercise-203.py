# Day 1 - Exercise 203
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-110', 'mfa_active': True},
    {'username': 'username-626', 'mfa_active': False},
    {'username': 'username-865', 'mfa_active': False},
    {'username': 'username-227', 'mfa_active': True},
    {'username': 'username-506', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

