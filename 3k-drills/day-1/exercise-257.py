# Day 1 - Exercise 257
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-453', 'cost': 3500},
    {'db_name': 'db-739', 'cost': 1200},
    {'db_name': 'db-360', 'cost': 3500},
    {'db_name': 'db-850', 'cost': 800}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-453
# db-739
# db-360
