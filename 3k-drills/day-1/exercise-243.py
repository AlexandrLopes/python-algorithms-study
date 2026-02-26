# Day 1 - Exercise 243
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-245', 'mfa_active': True},
    {'username': 'user-953', 'mfa_active': True},
    {'username': 'user-919', 'mfa_active': False},
    {'username': 'user-500', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-919
# user-500
