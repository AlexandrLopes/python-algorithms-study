# Day 1 - Exercise 43
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-542', 'mfa_active': True},
    {'username': 'user-607', 'mfa_active': True},
    {'username': 'user-484', 'mfa_active': False},
    {'username': 'user-107', 'mfa_active': False},
    {'username': 'user-916', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-484
# user-107
# user-916
