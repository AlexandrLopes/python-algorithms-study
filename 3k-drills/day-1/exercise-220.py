# Day 1 - Exercise 220
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-778', 'is_public': False},
    {'bucket_name': 'bucket-401', 'is_public': True},
    {'bucket_name': 'bucket-773', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-401
