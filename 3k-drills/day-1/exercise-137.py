# Day 1 - Exercise 137
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-641', 'mfa_active': False},
    {'username': 'username-362', 'mfa_active': False},
    {'username': 'username-279', 'mfa_active': True},
    {'username': 'username-726', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

