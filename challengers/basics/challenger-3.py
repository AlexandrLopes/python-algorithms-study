aws_billing_response = {
    "month": "February",
    "account_id": "111222333",
    "services": [
        {"service_name": "EC2", "region": "us-east-1", "costs": {"compute": 150.00, "storage": 50.00}},
        {"service_name": "S3", "region": "us-east-1", "costs": {"storage": 25.00}},
        {"service_name": "Lambda", "region": "us-east-1"}, 
        {"service_name": "RDS", "region": "sa-east-1", "costs": {"compute": 200.00, "storage": 100.00}}
    ]
}

services = aws_billing_response["services"]

for item in services:
    if item["region"] == "us-east-1":
        
        try:
            storage_cost = item["costs"]["storage"]
        except KeyError:
            storage_cost = 0.0
            
        print(f"Service {item['service_name']} has a storage cost of: ${storage_cost}")