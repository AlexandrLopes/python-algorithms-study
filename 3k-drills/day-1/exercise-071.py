# Day 1 - Exercise 71
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-941', 'mfa_active': False},
    {'username': 'user-772', 'mfa_active': False},
    {'username': 'user-851', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:



# -----------------------------------
# Expected Output:
# user-941
# user-772
# user-851
