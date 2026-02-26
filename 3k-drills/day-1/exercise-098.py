# Day 1 - Exercise 98
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-854', 'mfa_active': False},
    {'username': 'user-624', 'mfa_active': True},
    {'username': 'user-121', 'mfa_active': False},
    {'username': 'user-904', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-854
# user-121
# user-904
