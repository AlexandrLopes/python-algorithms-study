# Day 1 - Exercise 31
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-274', 'mfa_active': True},
    {'username': 'username-655', 'mfa_active': True},
    {'username': 'username-381', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

