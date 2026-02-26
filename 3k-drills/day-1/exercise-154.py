# Day 1 - Exercise 154
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-773', 'mfa_active': False},
    {'username': 'user-956', 'mfa_active': False},
    {'username': 'user-409', 'mfa_active': False},
    {'username': 'user-861', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-773
# user-956
# user-409
# user-861
