# Day 1 - Exercise 248
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-472', 'mfa_active': True},
    {'username': 'username-150', 'mfa_active': True},
    {'username': 'username-672', 'mfa_active': True},
    {'username': 'username-951', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

