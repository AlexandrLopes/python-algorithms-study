# Day 1 - Exercise 250
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-533', 'mfa_active': False},
    {'username': 'user-150', 'mfa_active': False},
    {'username': 'user-359', 'mfa_active': True},
    {'username': 'user-859', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-533
# user-150
# user-859
