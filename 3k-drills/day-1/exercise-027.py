# Day 1 - Exercise 27
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-198', 'mfa_active': False},
    {'username': 'user-230', 'mfa_active': False},
    {'username': 'user-461', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-198
# user-230
# user-461
