import os
import random

folder = "day-1"
os.makedirs(folder, exist_ok=True)

print("Regenerating Day 1 with Expected Outputs...")

for i in range(1, 301):
    file_path = f"{folder}/exercise-{i:03d}.py"
    
    # 1: EC2 Running, 2: S3 Public, 3: RDS Cost > 1000, 4: IAM MFA False
    choice = random.randint(1, 4)
    data_list = []
    expected_list = []
    
    if choice == 1:
        context = "Cloud Auditing. Find all EC2 instances that are currently 'running'."
        var = "ec2_instances"
        instruction = "Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'."
        for _ in range(random.randint(3, 5)):
            state = random.choice(["'running'", "'stopped'", "'terminated'"])
            inst_id = f"'i-{random.randint(100, 999)}'"
            data_list.append(f"    {{'id': {inst_id}, 'state': {state}}}")
            if state == "'running'": expected_list.append(f"# {inst_id.strip(chr(39))}")
            
    elif choice == 2:
        context = "Security Check. Identify S3 buckets exposed to the public."
        var = "s3_buckets"
        instruction = "Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True."
        for _ in range(random.randint(3, 5)):
            is_pub = random.choice(["True", "False"])
            b_name = f"'bucket-{random.randint(100, 999)}'"
            data_list.append(f"    {{'bucket_name': {b_name}, 'is_public': {is_pub}}}")
            if is_pub == "True": expected_list.append(f"# {b_name.strip(chr(39))}")
            
    elif choice == 3:
        context = "FinOps Routine. Find databases that cost more than $1000 a month."
        var = "rds_databases"
        instruction = "Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000."
        for _ in range(random.randint(3, 5)):
            cost = random.choice([250, 800, 1200, 3500])
            db_name = f"'db-{random.randint(100, 999)}'"
            data_list.append(f"    {{'db_name': {db_name}, 'cost': {cost}}}")
            if cost > 1000: expected_list.append(f"# {db_name.strip(chr(39))}")
            
    else:
        context = "IAM Compliance. List the usernames of users who do NOT have MFA enabled."
        var = "iam_users"
        instruction = "Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False."
        for _ in range(random.randint(3, 5)):
            mfa = random.choice(["True", "False"])
            uname = f"'user-{random.randint(100, 999)}'"
            data_list.append(f"    {{'username': {uname}, 'mfa_active': {mfa}}}")
            if mfa == "False": expected_list.append(f"# {uname.strip(chr(39))}")

    data_block = ",\n".join(data_list)
    
    # Se a aleatoriedade não gerar nenhum item que bata com o filtro, avisa no gabarito
    expected_block = "\n".join(expected_list) if expected_list else "# (No output expected for this specific random data)"
    
    with open(file_path, "w") as f:
        f.write(f"# Day 1 - Exercise {i}\n")
        f.write(f"# Context: {context}\n\n")
        f.write(f"{var} = [\n{data_block}\n]\n\n")
        f.write(f"# TODO: {instruction}\n")
        f.write("# Write your code below:\n\n\n\n")
        f.write(f"# -----------------------------------\n")
        f.write(f"# Expected Output:\n{expected_block}\n")

print("Day 1 Fixed! All exercises now have their Expected Output.")