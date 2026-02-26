# Day 1 - Exercise 138
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-478', 'cost': 1200},
    {'db_name': 'db-273', 'cost': 250},
    {'db_name': 'db-550', 'cost': 800},
    {'db_name': 'db-199', 'cost': 3500},
    {'db_name': 'db-222', 'cost': 1200}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:



# -----------------------------------
# Expected Output:
# db-478
# db-199
# db-222
