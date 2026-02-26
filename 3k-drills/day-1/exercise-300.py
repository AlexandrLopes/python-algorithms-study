# Day 1 - Exercise 300
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'username-364', 'mfa_active': True},
    {'username': 'username-228', 'mfa_active': False},
    {'username': 'username-838', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

