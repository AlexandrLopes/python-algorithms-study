# Day 1 - Exercise 222
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-625', 'cost': 800},
    {'db_name': 'db-832', 'cost': 1200},
    {'db_name': 'db-398', 'cost': 3500},
    {'db_name': 'db-248', 'cost': 1200},
    {'db_name': 'db-585', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])

# -----------------------------------
# Expected Output:
# db-832
# db-398
# db-248
# db-585
