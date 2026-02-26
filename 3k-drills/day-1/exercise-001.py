# Day 1 - Exercise 1
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-290', 'mfa_active': True},
    {'username': 'username-339', 'mfa_active': False},
    {'username': 'username-330', 'mfa_active': False},
    {'username': 'username-244', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

