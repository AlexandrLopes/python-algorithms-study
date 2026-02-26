import os
import random

# Garantir que a pasta existe
folder = "day-1"
os.makedirs(folder, exist_ok=True)

# Templates de exercícios focados em For + Dict + If
templates = [
    {
        "context": "Cloud Auditing. You need to find all EC2 instances that are currently 'running'.",
        "var_name": "ec2_instances",
        "keys": ["id", "state"],
        "condition_key": "state",
        "condition_val": "'running'",
        "instruction": "Write a for loop with an if statement. Print the 'id' ONLY if the 'state' is 'running'."
    },
    {
        "context": "Security Check. You must identify S3 buckets exposed to the public.",
        "var_name": "s3_buckets",
        "keys": ["bucket_name", "is_public"],
        "condition_key": "is_public",
        "condition_val": "True",
        "instruction": "Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True."
    },
    {
        "context": "FinOps Routine. Find databases that cost more than $1000 a month.",
        "var_name": "rds_databases",
        "keys": ["db_name", "cost"],
        "condition_key": "cost",
        "condition_val": "> 1000",
        "instruction": "Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000."
    },
    {
        "context": "IAM Compliance. List the usernames of users who do NOT have MFA enabled.",
        "var_name": "iam_users",
        "keys": ["username", "mfa_active"],
        "condition_key": "mfa_active",
        "condition_val": "False",
        "instruction": "Write a loop and an if statement. Print 'username' ONLY if 'mfa_active' is False."
    }
]

print("A gerar 300 exercícios únicos para o Day 1...")

for i in range(1, 301):
    file_path = f"{folder}/exercise-{i:03d}.py"
    
    # Escolhe um template à sorte
    t = random.choice(templates)
    
    # Gera dados aleatórios para não ser sempre igual
    data_list = []
    for _ in range(random.randint(3, 5)):
        if "cost" in t["keys"]:
            val2 = random.choice([250, 800, 1200, 3500])
        elif "is_public" in t["keys"] or "mfa_active" in t["keys"]:
            val2 = random.choice([True, False])
        else:
            val2 = random.choice(["'running'", "'stopped'", "'terminated'"])
            
        val1 = f"'{t['keys'][0]}-{random.randint(100, 999)}'"
        
        # Formata o dicionário como string
        dict_str = f"    {{'{t['keys'][0]}': {val1}, '{t['keys'][1]}': {val2}}}"
        data_list.append(dict_str)
        
    data_block = ",\n".join(data_list)
    
    # Escreve tudo dentro do ficheiro
    with open(file_path, "w") as f:
        f.write(f"# Day 1 - Exercise {i}\n")
        f.write(f"# Context: {t['context']}\n\n")
        f.write(f"{t['var_name']} = [\n{data_block}\n]\n\n")
        f.write(f"# TODO: {t['instruction']}\n")
        f.write("# Write your code below:\n\n")

print("Sucesso! Os 300 ficheiros do Day 1 estão prontos para resolver.")