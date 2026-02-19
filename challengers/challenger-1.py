aws_api_response = {
    "Region": "us-east-1",
    "Account": "1234567890",
    "Instances": [
        {"Id": "i-0a1b2c", "State": "running", "Tags": {"Name": "Web-Server-01", "Environment": "Production"}},
        {"Id": "i-0x9y8z", "State": "stopped"},
        {"Id": "i-0p1q2r", "State": "running", "Tags": {"Name": "Database-Main"}}
    ]
}

lista_de_servidores = aws_api_response["Instances"]

for servidor in lista_de_servidores:
    if servidor["State"] == "running":
        try:
            ambiente = servidor["Tags"]["Environment"]
        except KeyError:
            ambiente = "Unknown"
            
        print(f"Servidor {servidor['Id']} está no ambiente: {ambiente}")