print("Drill 1") #1
ec2_instances = [
    {"server_name": "Web-Production", "state": "running"},
    {"server_name": "Database-Main", "state": "stopped"},
    {"server_name": "Cache-Redis", "state": "running"}
]

for instance in ec2_instances:
    if instance["state"] == "running":
        print(f"Server {instance['server_name']} is running")

print("Drill 2") #2
s3_buckets = [
    {"bucket_name": "company-data", "size_gb": 150},
    {"bucket_name": "test-assets", "size_gb": 5},
    {"bucket_name": "backup-2025", "size_gb": 500},
    {"bucket_name": "empty-bucket", "size_gb": 0}
]

for bucket in s3_buckets:
    if bucket["size_gb"]>100:
        print(f"WARNING: {bucket['bucket_name']} is too large!")