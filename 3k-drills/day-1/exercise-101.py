# Day 1 - Exercise 101
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-380', 'cost': 1200},
    {'db_name': 'db-366', 'cost': 3500},
    {'db_name': 'db-858', 'cost': 3500},
    {'db_name': 'db-585', 'cost': 3500},
    {'db_name': 'db-287', 'cost': 250}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-380
# db-366
# db-858
# db-585
