# Day 1 - Exercise 218
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-940', 'mfa_active': False},
    {'username': 'username-921', 'mfa_active': False},
    {'username': 'username-193', 'mfa_active': False},
    {'username': 'username-283', 'mfa_active': True},
    {'username': 'username-706', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

