# Day 1 - Exercise 300
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-606', 'mfa_active': True},
    {'username': 'user-973', 'mfa_active': True},
    {'username': 'user-644', 'mfa_active': True},
    {'username': 'user-241', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-241
