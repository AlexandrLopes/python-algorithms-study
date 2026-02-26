# Day 1 - Exercise 121
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-506', 'is_public': False},
    {'bucket_name': 'bucket-471', 'is_public': False},
    {'bucket_name': 'bucket-576', 'is_public': False},
    {'bucket_name': 'bucket-110', 'is_public': True},
    {'bucket_name': 'bucket-119', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-110
# bucket-119
