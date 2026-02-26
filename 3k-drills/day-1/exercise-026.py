# Day 1 - Exercise 26
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-422', 'mfa_active': True},
    {'username': 'user-276', 'mfa_active': False},
    {'username': 'user-967', 'mfa_active': True},
    {'username': 'user-497', 'mfa_active': True},
    {'username': 'user-433', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["username"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-276
# user-433
