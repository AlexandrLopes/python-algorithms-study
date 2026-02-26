# Day 1 - Exercise 48
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-165', 'mfa_active': True},
    {'username': 'user-214', 'mfa_active': False},
    {'username': 'user-359', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-214
# user-359
