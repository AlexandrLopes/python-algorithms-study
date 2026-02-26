# Day 1 - Exercise 100
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-784', 'cost': 250},
    {'db_name': 'db-353', 'cost': 250},
    {'db_name': 'db-456', 'cost': 3500},
    {'db_name': 'db-377', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-456
# db-377
