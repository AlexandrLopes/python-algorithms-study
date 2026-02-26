# Day 1 - Exercise 153
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-293', 'mfa_active': True},
    {'username': 'user-980', 'mfa_active': True},
    {'username': 'user-265', 'mfa_active': False},
    {'username': 'user-244', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-265
# user-244
