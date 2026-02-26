# Day 1 - Exercise 190
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-243', 'cost': 3500},
    {'db_name': 'db-227', 'cost': 250},
    {'db_name': 'db-652', 'cost': 1200},
    {'db_name': 'db-855', 'cost': 3500},
    {'db_name': 'db-503', 'cost': 250}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-243
# db-652
# db-855
