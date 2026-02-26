# Day 1 - Exercise 22
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-953', 'mfa_active': False},
    {'username': 'username-576', 'mfa_active': True},
    {'username': 'username-961', 'mfa_active': True},
    {'username': 'username-245', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

