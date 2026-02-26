# Day 1 - Exercise 80
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-190', 'mfa_active': True},
    {'username': 'username-554', 'mfa_active': False},
    {'username': 'username-637', 'mfa_active': False},
    {'username': 'username-838', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

