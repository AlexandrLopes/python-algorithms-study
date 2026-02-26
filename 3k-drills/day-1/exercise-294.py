# Day 1 - Exercise 294
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-383', 'mfa_active': True},
    {'username': 'username-139', 'mfa_active': True},
    {'username': 'username-737', 'mfa_active': True},
    {'username': 'username-777', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

