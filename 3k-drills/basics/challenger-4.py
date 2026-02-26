print("Drill 1") #1
cloud_providers = ["AWS", "Azure", "Google Cloud"]

for n in cloud_providers:
    print(f"Provider:",n)

print("Drill 2") #2
server_status = ["running", "stopped", "running", "terminated"]

for i in server_status:
    if i == "running":
        print("The server is running")

print("Drill 3") #3
user_profile = {
    "username": "alexandre_cloud",
    "role": "Engineer",
    "active": True
}

current_role = user_profile["role"]
print(f"User role is: {current_role}")