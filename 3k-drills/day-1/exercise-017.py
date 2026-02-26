# Day 1 - Exercise 17
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-183', 'mfa_active': False},
    {'username': 'user-281', 'mfa_active': False},
    {'username': 'user-426', 'mfa_active': False},
    {'username': 'user-519', 'mfa_active': False},
    {'username': 'user-306', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-183
# user-281
# user-426
# user-519
# user-306
