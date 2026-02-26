# Day 1 - Exercise 125
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-345', 'mfa_active': False},
    {'username': 'user-634', 'mfa_active': True},
    {'username': 'user-285', 'mfa_active': True},
    {'username': 'user-815', 'mfa_active': False},
    {'username': 'user-843', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-345
# user-815
