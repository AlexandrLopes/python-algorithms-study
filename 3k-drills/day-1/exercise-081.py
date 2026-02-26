# Day 1 - Exercise 81
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-475', 'mfa_active': False},
    {'username': 'user-749', 'mfa_active': True},
    {'username': 'user-331', 'mfa_active': False},
    {'username': 'user-868', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-475
# user-331
