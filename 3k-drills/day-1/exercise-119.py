# Day 1 - Exercise 119
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-161', 'mfa_active': True},
    {'username': 'username-611', 'mfa_active': True},
    {'username': 'username-909', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

