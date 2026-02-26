"""

aws_iam_response = {
    "account_alias": "my-company-prod",
    "users": [
        {"user_id": "admin_01", "status": "active", "settings": {"mfa_active": True, "cli_access": True}},
        {"user_id": "dev_02", "status": "inactive", "settings": {"mfa_active": False}},
        {"user_id": "dev_03", "status": "active"} 
    ]
}
"""

aws_api_response = {
    "Region": "us-east-1",
    "Account": "1234567890",
    "Instances": [
        {"Id": "i-0a1b2c", "State": "running", "Tags": {"Name": "Web-Server-01", "Environment": "Production"}},
        {"Id": "i-0x9y8z", "State": "stopped"},
        {"Id": "i-0p1q2r", "State": "running", "Tags": {"Name": "Database-Main"}}
    ]
}

server_list = aws_api_response["Instances"]

for server in server_list:
    if server["State"] == "running":
        
        try:
            environment = server["Tags"]["Environment"]
        except KeyError:
            environment = "Unknown"
            
        print(f"Server {server['Id']} is in environment: {environment}")

