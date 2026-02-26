# Day 1 - Exercise 7
# Context: IAM Compliance. List the usernames of users who do NOT have MFA enabled.

iam_users = [
    {'username': 'user-874', 'mfa_active': True},
    {'username': 'user-280', 'mfa_active': True},
    {'username': 'user-996', 'mfa_active': True},
    {'username': 'user-121', 'mfa_active': False},
    {'username': 'user-196', 'mfa_active': True}
]

# TODO: Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False.
# Write your code below:

for name in iam_users:
    if name["mfa_active"] == False:
        print(name["username"])


# -----------------------------------
# Expected Output:
# user-121
