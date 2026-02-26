# Day 1 - Exercise 149
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-616', 'cost': 800},
    {'db_name': 'db-940', 'cost': 3500},
    {'db_name': 'db-602', 'cost': 800},
    {'db_name': 'db-176', 'cost': 3500},
    {'db_name': 'db-683', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-940
# db-176
# db-683
