# Day 1 - Exercise 89
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-922', 'mfa_active': True},
    {'username': 'user-302', 'mfa_active': False},
    {'username': 'user-929', 'mfa_active': False},
    {'username': 'user-604', 'mfa_active': True},
    {'username': 'user-405', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-302
# user-929
# user-405
