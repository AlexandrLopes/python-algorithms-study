# Day 1 - Exercise 180
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-141', 'mfa_active': False},
    {'username': 'user-723', 'mfa_active': True},
    {'username': 'user-279', 'mfa_active': False},
    {'username': 'user-805', 'mfa_active': False},
    {'username': 'user-146', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-141
# user-279
# user-805
