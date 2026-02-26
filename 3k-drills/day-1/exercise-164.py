# Day 1 - Exercise 164
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-821', 'mfa_active': False},
    {'username': 'username-767', 'mfa_active': False},
    {'username': 'username-978', 'mfa_active': True},
    {'username': 'username-710', 'mfa_active': True},
    {'username': 'username-610', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

