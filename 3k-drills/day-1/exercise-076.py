# Day 1 - Exercise 76
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-801', 'cost': 800},
    {'db_name': 'db-705', 'cost': 1200},
    {'db_name': 'db-331', 'cost': 250},
    {'db_name': 'db-192', 'cost': 250},
    {'db_name': 'db-736', 'cost': 1200}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-705
# db-736
