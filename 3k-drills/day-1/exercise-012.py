# Day 1 - Exercise 12
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-326', 'mfa_active': True},
    {'username': 'user-900', 'mfa_active': False},
    {'username': 'user-662', 'mfa_active': False},
    {'username': 'user-660', 'mfa_active': True},
    {'username': 'user-443', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-900
# user-662
