# Day 1 - Exercise 264
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-346', 'mfa_active': False},
    {'username': 'username-242', 'mfa_active': True},
    {'username': 'username-353', 'mfa_active': False},
    {'username': 'username-863', 'mfa_active': False},
    {'username': 'username-519', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

