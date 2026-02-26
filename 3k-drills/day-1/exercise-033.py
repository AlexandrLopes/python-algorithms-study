# Day 1 - Exercise 33
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-464', 'mfa_active': True},
    {'username': 'username-989', 'mfa_active': False},
    {'username': 'username-519', 'mfa_active': False},
    {'username': 'username-391', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

