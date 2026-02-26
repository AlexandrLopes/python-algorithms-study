# Day 1 - Exercise 295
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-595', 'mfa_active': False},
    {'username': 'username-290', 'mfa_active': False},
    {'username': 'username-228', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

