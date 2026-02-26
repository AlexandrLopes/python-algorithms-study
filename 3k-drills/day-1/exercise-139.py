# Day 1 - Exercise 139
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-609', 'mfa_active': False},
    {'username': 'username-377', 'mfa_active': False},
    {'username': 'username-645', 'mfa_active': False},
    {'username': 'username-806', 'mfa_active': True},
    {'username': 'username-757', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

