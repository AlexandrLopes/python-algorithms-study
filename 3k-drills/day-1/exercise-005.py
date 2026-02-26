# Day 1 - Exercise 5
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-974', 'mfa_active': False},
    {'username': 'user-424', 'mfa_active': False},
    {'username': 'user-453', 'mfa_active': False},
    {'username': 'user-900', 'mfa_active': True},
    {'username': 'user-897', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-974
# user-424
# user-453
# user-897
