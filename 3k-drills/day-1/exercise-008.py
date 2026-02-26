# Day 1 - Exercise 8
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-106', 'mfa_active': True},
    {'username': 'username-450', 'mfa_active': False},
    {'username': 'username-194', 'mfa_active': True},
    {'username': 'username-414', 'mfa_active': True},
    {'username': 'username-169', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

