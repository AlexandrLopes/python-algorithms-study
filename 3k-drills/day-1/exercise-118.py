# Day 1 - Exercise 118
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-535', 'mfa_active': True},
    {'username': 'username-689', 'mfa_active': True},
    {'username': 'username-626', 'mfa_active': True},
    {'username': 'username-388', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

