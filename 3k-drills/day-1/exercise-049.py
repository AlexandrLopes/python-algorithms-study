# Day 1 - Exercise 49
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-191', 'mfa_active': False},
    {'username': 'username-716', 'mfa_active': False},
    {'username': 'username-688', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

