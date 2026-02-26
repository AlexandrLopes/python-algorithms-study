# Day 1 - Exercise 42
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-979', 'mfa_active': False},
    {'username': 'user-914', 'mfa_active': True},
    {'username': 'user-133', 'mfa_active': False},
    {'username': 'user-717', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-979
# user-133
# user-717
