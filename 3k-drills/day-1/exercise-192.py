# Day 1 - Exercise 192
# Context: FinOps Routine. Find databases that cost more than $1000 a month.

rds_databases = [
    {'db_name': 'db-911', 'cost': 1200},
    {'db_name': 'db-989', 'cost': 1200},
    {'db_name': 'db-966', 'cost': 3500},
    {'db_name': 'db-686', 'cost': 800}
]

# TODO: Write a loop. Print the 'db_name' ONLY if the 'cost' is greater than 1000.
# Write your code below:
for name in rds_databases:
    if name["cost"] > 1000:
        print(name["db_name"])


# -----------------------------------
# Expected Output:
# db-911
# db-989
# db-966
