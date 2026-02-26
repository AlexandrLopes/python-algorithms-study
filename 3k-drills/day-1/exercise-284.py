# Day 1 - Exercise 284
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-691', 'cost': 800},
    {'db_name': 'db-134', 'cost': 800},
    {'db_name': 'db-860', 'cost': 250},
    {'db_name': 'db-459', 'cost': 250},
    {'db_name': 'db-822', 'cost': 800}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
