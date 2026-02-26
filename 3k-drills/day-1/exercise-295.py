# Day 1 - Exercise 295
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-866', 'cost': 800},
    {'db_name': 'db-107', 'cost': 1200},
    {'db_name': 'db-286', 'cost': 800},
    {'db_name': 'db-576', 'cost': 1200},
    {'db_name': 'db-600', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:



# -----------------------------------
# Expected Output:
# db-107
# db-576
# db-600
