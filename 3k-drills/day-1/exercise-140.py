# Day 1 - Exercise 140
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-539', 'mfa_active': False},
    {'username': 'user-639', 'mfa_active': True},
    {'username': 'user-847', 'mfa_active': False},
    {'username': 'user-180', 'mfa_active': False},
    {'username': 'user-784', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-539
# user-847
# user-180
