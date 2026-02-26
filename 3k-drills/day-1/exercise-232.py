# Day 1 - Exercise 232
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-525', 'mfa_active': True},
    {'username': 'user-152', 'mfa_active': False},
    {'username': 'user-577', 'mfa_active': False},
    {'username': 'user-383', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])

# -----------------------------------
# Expected Output:
# user-152
# user-577
# user-383
