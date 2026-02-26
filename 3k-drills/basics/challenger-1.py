
"""
Write a for loop that goes through all instances in this list 
and prints the ID Environment only for servers whose State is equal to “running.”

aws_api_response = {
    "Region": "us-east-1",
    "Account": "1234567890",
    "Instances": [
        {
            "Id": "i-0a1b2c", 
            "State": "running", 
            "Tags": {"Name": "Web-Server-01", "Environment": "Production"}
        },
        {
            "Id": "i-0x9y8z", 
            "State": "stopped" 
            # Repare que este servidor não tem a chave "Tags"
        },
        {
            "Id": "i-0p1q2r", 
            "State": "running", 
            "Tags": {"Name": "Database-Main"} 
            # Repare que este tem "Tags", mas não tem a chave "Environment"
        }
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