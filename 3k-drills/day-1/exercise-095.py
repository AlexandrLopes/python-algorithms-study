# Day 1 - Exercise 95
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-650', 'mfa_active': False},
    {'username': 'user-598', 'mfa_active': False},
    {'username': 'user-644', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-650
# user-598
