# Day 1 - Exercise 239
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-678', 'cost': 800},
    {'db_name': 'db-683', 'cost': 800},
    {'db_name': 'db-287', 'cost': 1200},
    {'db_name': 'db-742', 'cost': 1200}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-287
# db-742
