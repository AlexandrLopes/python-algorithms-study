# Day 1 - Exercise 127
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-487', 'mfa_active': False},
    {'username': 'user-695', 'mfa_active': True},
    {'username': 'user-425', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-487
