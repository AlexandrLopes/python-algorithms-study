# Day 1 - Exercise 151
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-108', 'mfa_active': False},
    {'username': 'user-669', 'mfa_active': True},
    {'username': 'user-593', 'mfa_active': True},
    {'username': 'user-865', 'mfa_active': True},
    {'username': 'user-435', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-108
