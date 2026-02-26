# Day 1 - Exercise 233
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-396', 'cost': 1200},
    {'db_name': 'db-998', 'cost': 250},
    {'db_name': 'db-183', 'cost': 3500},
    {'db_name': 'db-660', 'cost': 250},
    {'db_name': 'db-485', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:



# -----------------------------------
# Expected Output:
# db-396
# db-183
# db-485
