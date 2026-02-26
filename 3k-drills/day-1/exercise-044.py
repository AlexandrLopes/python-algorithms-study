# Day 1 - Exercise 44
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-917', 'mfa_active': True},
    {'username': 'user-772', 'mfa_active': False},
    {'username': 'user-440', 'mfa_active': True},
    {'username': 'user-273', 'mfa_active': False},
    {'username': 'user-474', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-772
# user-273
