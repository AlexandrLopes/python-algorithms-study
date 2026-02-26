# Day 1 - Exercise 244
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-381', 'mfa_active': False},
    {'username': 'user-835', 'mfa_active': False},
    {'username': 'user-874', 'mfa_active': False},
    {'username': 'user-173', 'mfa_active': False},
    {'username': 'user-890', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-381
# user-835
# user-874
# user-173
