# Day 1 - Exercise 218
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-252', 'mfa_active': True},
    {'username': 'user-352', 'mfa_active': True},
    {'username': 'user-273', 'mfa_active': False},
    {'username': 'user-343', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-273
# user-343
