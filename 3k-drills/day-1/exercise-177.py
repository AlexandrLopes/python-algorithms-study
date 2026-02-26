# Day 1 - Exercise 177
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-519', 'mfa_active': False},
    {'username': 'user-295', 'mfa_active': True},
    {'username': 'user-409', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-519
# user-409
