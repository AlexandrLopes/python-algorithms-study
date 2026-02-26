# Day 1 - Exercise 75
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-628', 'is_public': False},
    {'bucket_name': 'bucket-610', 'is_public': True},
    {'bucket_name': 'bucket-273', 'is_public': True},
    {'bucket_name': 'bucket-859', 'is_public': False},
    {'bucket_name': 'bucket-775', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-610
# bucket-273
