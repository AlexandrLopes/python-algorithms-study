# Day 1 - Exercise 18
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-564', 'mfa_active': False},
    {'username': 'user-488', 'mfa_active': True},
    {'username': 'user-534', 'mfa_active': False},
    {'username': 'user-894', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-564
# user-534
# user-894
