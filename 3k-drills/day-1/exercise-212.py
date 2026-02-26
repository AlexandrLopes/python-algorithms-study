# Day 1 - Exercise 212
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-790', 'mfa_active': False},
    {'username': 'user-289', 'mfa_active': False},
    {'username': 'user-701', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-790
# user-289
