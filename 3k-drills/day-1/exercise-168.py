# Day 1 - Exercise 168
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-251', 'mfa_active': False},
    {'username': 'username-536', 'mfa_active': True},
    {'username': 'username-347', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

