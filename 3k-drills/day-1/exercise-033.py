# Day 1 - Exercise 33
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-540', 'cost': 3500},
    {'db_name': 'db-443', 'cost': 1200},
    {'db_name': 'db-981', 'cost': 250},
    {'db_name': 'db-626', 'cost': 3500},
    {'db_name': 'db-157', 'cost': 800}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-540
# db-443
# db-626
