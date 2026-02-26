# Day 1 - Exercise 276
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-930', 'mfa_active': True},
    {'username': 'user-619', 'mfa_active': True},
    {'username': 'user-773', 'mfa_active': True},
    {'username': 'user-261', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-261
