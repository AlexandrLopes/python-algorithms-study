# Day 1 - Exercise 144
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-665', 'mfa_active': False},
    {'username': 'user-133', 'mfa_active': True},
    {'username': 'user-757', 'mfa_active': True},
    {'username': 'user-658', 'mfa_active': True},
    {'username': 'user-576', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-665
