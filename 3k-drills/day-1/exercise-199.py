# Day 1 - Exercise 199
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-717', 'mfa_active': True},
    {'username': 'username-293', 'mfa_active': True},
    {'username': 'username-467', 'mfa_active': False},
    {'username': 'username-151', 'mfa_active': True},
    {'username': 'username-788', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

