# Day 1 - Exercise 68
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-221', 'mfa_active': False},
    {'username': 'user-328', 'mfa_active': False},
    {'username': 'user-252', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["username"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-221
# user-328
# user-252
