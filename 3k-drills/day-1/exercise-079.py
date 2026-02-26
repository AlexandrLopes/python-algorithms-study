# Day 1 - Exercise 79
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-636', 'cost': 800},
    {'db_name': 'db-660', 'cost': 250},
    {'db_name': 'db-945', 'cost': 250},
    {'db_name': 'db-210', 'cost': 250},
    {'db_name': 'db-396', 'cost': 250}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
