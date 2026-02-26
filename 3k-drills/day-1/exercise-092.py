# Day 1 - Exercise 92
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-128', 'cost': 1200},
    {'db_name': 'db-203', 'cost': 800},
    {'db_name': 'db-402', 'cost': 250},
    {'db_name': 'db-967', 'cost': 800}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:

for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])

# -----------------------------------
# Expected Output:
# db-128
