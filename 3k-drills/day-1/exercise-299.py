# Day 1 - Exercise 299
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-589', 'mfa_active': True},
    {'username': 'username-227', 'mfa_active': False},
    {'username': 'username-941', 'mfa_active': True},
    {'username': 'username-408', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

