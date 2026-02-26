# Day 1 - Exercise 123
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-687', 'cost': 3500},
    {'db_name': 'db-195', 'cost': 800},
    {'db_name': 'db-843', 'cost': 250},
    {'db_name': 'db-865', 'cost': 3500},
    {'db_name': 'db-868', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-687
# db-865
# db-868
