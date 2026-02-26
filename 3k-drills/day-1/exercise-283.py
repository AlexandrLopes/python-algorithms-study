# Day 1 - Exercise 283
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-435', 'mfa_active': False},
    {'username': 'username-618', 'mfa_active': False},
    {'username': 'username-200', 'mfa_active': False},
    {'username': 'username-312', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

