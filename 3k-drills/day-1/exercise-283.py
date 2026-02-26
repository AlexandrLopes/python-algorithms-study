# Day 1 - Exercise 283
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-918', 'mfa_active': True},
    {'username': 'user-775', 'mfa_active': True},
    {'username': 'user-264', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-264
