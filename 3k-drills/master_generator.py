import os
import random

# The Bootcamp Syllabus and Data Factory
bootcamp_days = {
    2: {
        "theme": "Nested Loops (List inside Dict)",
        "context": "Network Map. You have a list of VPCs, and each VPC has a list of subnets.",
        "data_setup": "vpcs = [\n    {'vpc_id': 'vpc-1A', 'subnets': ['sub-1', 'sub-2']},\n    {'vpc_id': 'vpc-2B', 'subnets': ['sub-3']}\n]",
        "instruction": "Write a nested loop (a loop inside a loop). First loop through the VPCs, then loop through the 'subnets' of each VPC. Print every subnet ID.",
        "expected": "sub-1\n# sub-2\n# sub-3"
    },
    3: {
        "theme": "Exception Handling (KeyError)",
        "context": "Tagging Audit. Some EC2 instances are missing the 'Tags' key entirely.",
        "data_setup": "instances = [\n    {'id': 'i-01', 'Tags': {'Env': 'Prod'}},\n    {'id': 'i-02'},\n    {'id': 'i-03', 'Tags': {'Env': 'Dev'}}\n]",
        "instruction": "Loop through the instances. Use try/except. Print the 'Env' tag. If KeyError occurs, print 'Untagged'.",
        "expected": "Prod\n# Untagged\n# Dev"
    },
    4: {
        "theme": "List Comprehension",
        "context": "Quick Filtering. You need to isolate stopped servers in a single line of code.",
        "data_setup": "servers = ['running', 'stopped', 'stopped', 'running']",
        "instruction": "Use list comprehension to create a new list called 'stopped_servers' containing only 'stopped'. Print the new list.",
        "expected": "['stopped', 'stopped']"
    },
    5: {
        "theme": "Dictionary Comprehension",
        "context": "Mapping Resources. You need to map server IDs to a default status.",
        "data_setup": "server_ids = ['i-111', 'i-222', 'i-333']",
        "instruction": "Use dictionary comprehension to create a dict where the key is the ID and the value is 'monitored'. Print the dict.",
        "expected": "{'i-111': 'monitored', 'i-222': 'monitored', 'i-333': 'monitored'}"
    },
    6: {
        "theme": "String Manipulation",
        "context": "ARN Parsing. You need to extract just the username from an AWS ARN string.",
        "data_setup": "user_arn = 'arn:aws:iam::123456789:user/alexandre_admin'",
        "instruction": "Use the .split() method to isolate the username ('alexandre_admin') from the string. Print it.",
        "expected": "alexandre_admin"
    },
    7: {
        "theme": "Data Type Casting",
        "context": "Billing API Fix. The API returned costs as strings, but you need them as floats to sum them.",
        "data_setup": "costs = ['10.50', '20.00', '5.25']",
        "instruction": "Loop through the list, convert each string to a float using float(), and add it to a 'total' variable. Print the total.",
        "expected": "35.75"
    },
    8: {
        "theme": "Functions (Modularity)",
        "context": "Reusability. Create a function that calculates total storage cost.",
        "data_setup": "# No data setup needed, build the function.",
        "instruction": "Define a function named 'get_cost' that takes 'gb_size' and 'price_per_gb'. Return the multiplication. Call it with (100, 0.02) and print.",
        "expected": "2.0"
    },
    9: {
        "theme": "Filtering Complex Lists",
        "context": "Advanced Search. Find users who are active AND have admin privileges.",
        "data_setup": "users = [\n    {'user': 'u1', 'active': True, 'admin': False},\n    {'user': 'u2', 'active': True, 'admin': True}\n]",
        "instruction": "Loop through users. Use an 'if' statement with 'and' to print the user ONLY if active is True and admin is True.",
        "expected": "u2"
    },
    10: {
        "theme": "Data Aggregation (The Boss)",
        "context": "Cost Grouping. Sum the costs by service type.",
        "data_setup": "resources = [\n    {'service': 'EC2', 'cost': 50},\n    {'service': 'S3', 'cost': 20},\n    {'service': 'EC2', 'cost': 30}\n]",
        "instruction": "Create an empty dict 'totals'. Loop resources. If service is in totals, add cost. Else, set cost. Print totals.",
        "expected": "{'EC2': 80, 'S3': 20}"
    }
}

print("Starting Master Generation for Day 2 to Day 10...")

for day in range(2, 11):
    folder_name = f"day-{day}"
    os.makedirs(folder_name, exist_ok=True)
    
    config = bootcamp_days[day]
    
    for ex in range(1, 301):
        file_path = f"{folder_name}/exercise-{ex:03d}.py"
        
        # Adding some randomness to make exercises feel fresh but logic identical
        random_id = random.randint(100, 999)
        
        with open(file_path, "w") as file:
            file.write(f"# Day {day} - Exercise {ex} | ID: {random_id}\n")
            file.write(f"# Theme: {config['theme']}\n")
            file.write(f"# Context: {config['context']}\n\n")
            file.write(f"{config['data_setup']}\n\n")
            file.write(f"# TODO: {config['instruction']}\n")
            file.write("# Write your code below:\n\n\n\n")
            file.write(f"# -----------------------------------\n")
            file.write(f"# Expected Output:\n# {config['expected']}\n")
            
    print(f"[{folder_name}] created successfully with 300 exercises.")

print("\nAll 2700 remaining drills have been successfully deployed. Let the grind begin!")