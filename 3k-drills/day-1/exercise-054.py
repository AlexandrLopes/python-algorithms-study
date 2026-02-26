# Day 1 - Exercise 54
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-567', 'mfa_active': True},
    {'username': 'username-871', 'mfa_active': True},
    {'username': 'username-407', 'mfa_active': False},
    {'username': 'username-553', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

