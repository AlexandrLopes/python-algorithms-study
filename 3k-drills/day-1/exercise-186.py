# Day 1 - Exercise 186
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-775', 'mfa_active': True},
    {'username': 'username-324', 'mfa_active': True},
    {'username': 'username-475', 'mfa_active': True},
    {'username': 'username-549', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

