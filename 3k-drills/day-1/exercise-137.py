# Day 1 - Exercise 137
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-874', 'mfa_active': False},
    {'username': 'user-742', 'mfa_active': True},
    {'username': 'user-915', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-874
# user-915
