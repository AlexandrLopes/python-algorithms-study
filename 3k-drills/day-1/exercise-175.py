# Day 1 - Exercise 175
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-957', 'mfa_active': False},
    {'username': 'user-194', 'mfa_active': True},
    {'username': 'user-299', 'mfa_active': False},
    {'username': 'user-224', 'mfa_active': True},
    {'username': 'user-535', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-957
# user-299
