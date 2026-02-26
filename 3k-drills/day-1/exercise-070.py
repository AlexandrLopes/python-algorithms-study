# Day 1 - Exercise 70
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-918', 'cost': 800},
    {'db_name': 'db-958', 'cost': 1200},
    {'db_name': 'db-647', 'cost': 3500},
    {'db_name': 'db-418', 'cost': 1200},
    {'db_name': 'db-273', 'cost': 250}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-958
# db-647
# db-418
