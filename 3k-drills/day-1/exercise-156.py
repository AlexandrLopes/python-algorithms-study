# Day 1 - Exercise 156
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-600', 'mfa_active': True},
    {'username': 'user-698', 'mfa_active': True},
    {'username': 'user-842', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
