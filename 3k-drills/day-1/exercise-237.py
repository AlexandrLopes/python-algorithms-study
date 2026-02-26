# Day 1 - Exercise 237
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-130', 'cost': 800},
    {'db_name': 'db-672', 'cost': 800},
    {'db_name': 'db-418', 'cost': 3500},
    {'db_name': 'db-665', 'cost': 1200},
    {'db_name': 'db-146', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:



# -----------------------------------
# Expected Output:
# db-418
# db-665
# db-146
