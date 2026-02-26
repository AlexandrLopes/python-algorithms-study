# Day 1 - Exercise 6
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-935', 'mfa_active': True},
    {'username': 'username-396', 'mfa_active': False},
    {'username': 'username-236', 'mfa_active': False},
    {'username': 'username-318', 'mfa_active': True},
    {'username': 'username-404', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

