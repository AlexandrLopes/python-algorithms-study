# Day 1 - Exercise 1
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-340', 'mfa_active': False},
    {'username': 'user-691', 'mfa_active': False},
    {'username': 'user-736', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-340
# user-691
