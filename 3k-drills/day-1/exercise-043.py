# Day 1 - Exercise 43
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-240', 'mfa_active': True},
    {'username': 'username-515', 'mfa_active': True},
    {'username': 'username-844', 'mfa_active': False},
    {'username': 'username-707', 'mfa_active': True},
    {'username': 'username-140', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

