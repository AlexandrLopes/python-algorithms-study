# Day 1 - Exercise 229
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-998', 'mfa_active': True},
    {'username': 'username-860', 'mfa_active': False},
    {'username': 'username-310', 'mfa_active': True},
    {'username': 'username-193', 'mfa_active': True},
    {'username': 'username-821', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

