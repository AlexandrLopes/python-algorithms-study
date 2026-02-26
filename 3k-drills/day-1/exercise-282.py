# Day 1 - Exercise 282
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-749', 'mfa_active': True},
    {'username': 'user-735', 'mfa_active': False},
    {'username': 'user-109', 'mfa_active': True},
    {'username': 'user-599', 'mfa_active': True},
    {'username': 'user-711', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-735
# user-711
