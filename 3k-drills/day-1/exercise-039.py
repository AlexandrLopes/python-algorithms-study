# Day 1 - Exercise 39
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-211', 'mfa_active': False},
    {'username': 'user-544', 'mfa_active': False},
    {'username': 'user-341', 'mfa_active': True},
    {'username': 'user-880', 'mfa_active': False}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:
for user in iam_users:
    if user["mfa_active"] == False:
        print(user["username"])


# -----------------------------------
# Expected Output:
# user-211
# user-544
# user-880
