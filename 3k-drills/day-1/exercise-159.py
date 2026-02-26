# Day 1 - Exercise 159
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-207', 'mfa_active': False},
    {'username': 'username-125', 'mfa_active': True},
    {'username': 'username-400', 'mfa_active': True},
    {'username': 'username-939', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

