# Day 1 - Exercise 293
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-147', 'mfa_active': False},
    {'username': 'username-358', 'mfa_active': False},
    {'username': 'username-757', 'mfa_active': True},
    {'username': 'username-276', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

