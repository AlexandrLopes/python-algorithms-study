# Day 1 - Exercise 126
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-266', 'mfa_active': False},
    {'username': 'username-593', 'mfa_active': True},
    {'username': 'username-759', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

