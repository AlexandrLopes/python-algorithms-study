# Day 1 - Exercise 21
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-840', 'cost': 1200},
    {'db_name': 'db-593', 'cost': 800},
    {'db_name': 'db-113', 'cost': 250},
    {'db_name': 'db-602', 'cost': 1200},
    {'db_name': 'db-901', 'cost': 3500}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:



# -----------------------------------
# Expected Output:
# db-840
# db-602
# db-901
