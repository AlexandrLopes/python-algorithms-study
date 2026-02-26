# Day 1 - Exercise 46
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-467', 'mfa_active': False},
    {'username': 'username-206', 'mfa_active': True},
    {'username': 'username-746', 'mfa_active': True},
    {'username': 'username-785', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

