# Day 1 - Exercise 183
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-141', 'mfa_active': True},
    {'username': 'user-774', 'mfa_active': False},
    {'username': 'user-820', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-774
# user-820
