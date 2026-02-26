# Day 1 - Exercise 31
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-379', 'mfa_active': False},
    {'username': 'user-822', 'mfa_active': True},
    {'username': 'user-981', 'mfa_active': False},
    {'username': 'user-253', 'mfa_active': True},
    {'username': 'user-317', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-379
# user-981
# user-317
