# Day 1 - Exercise 116
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-317', 'mfa_active': True},
    {'username': 'username-962', 'mfa_active': True},
    {'username': 'username-777', 'mfa_active': False},
    {'username': 'username-660', 'mfa_active': True},
    {'username': 'username-816', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

