# Day 1 - Exercise 152
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-647', 'mfa_active': True},
    {'username': 'user-502', 'mfa_active': False},
    {'username': 'user-312', 'mfa_active': True},
    {'username': 'user-547', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-502
