# Day 1 - Exercise 147
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-134', 'mfa_active': False},
    {'username': 'user-216', 'mfa_active': True},
    {'username': 'user-727', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-134
# user-727
