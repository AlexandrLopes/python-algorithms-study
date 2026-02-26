# Day 1 - Exercise 249
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-564', 'mfa_active': False},
    {'username': 'user-652', 'mfa_active': False},
    {'username': 'user-335', 'mfa_active': False},
    {'username': 'user-144', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-564
# user-652
# user-335
