# Day 1 - Exercise 36
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-287', 'mfa_active': True},
    {'username': 'user-685', 'mfa_active': False},
    {'username': 'user-305', 'mfa_active': False},
    {'username': 'user-366', 'mfa_active': False},
    {'username': 'user-536', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-685
# user-305
# user-366
# user-536
