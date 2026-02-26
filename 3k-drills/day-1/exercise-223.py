# Day 1 - Exercise 223
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-567', 'mfa_active': True},
    {'username': 'username-212', 'mfa_active': True},
    {'username': 'username-596', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

