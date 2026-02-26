# Day 1 - Exercise 141
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-693', 'cost': 250},
    {'db_name': 'db-411', 'cost': 1200},
    {'db_name': 'db-934', 'cost': 1200},
    {'db_name': 'db-262', 'cost': 800}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-411
# db-934
