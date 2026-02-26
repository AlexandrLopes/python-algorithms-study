# Day 1 - Exercise 35
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-318', 'mfa_active': False},
    {'username': 'username-553', 'mfa_active': True},
    {'username': 'username-629', 'mfa_active': False},
    {'username': 'username-646', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

