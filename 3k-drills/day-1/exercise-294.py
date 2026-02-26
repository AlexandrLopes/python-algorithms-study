# Day 1 - Exercise 294
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-449', 'is_public': False},
    {'bucket_name': 'bucket-326', 'is_public': False},
    {'bucket_name': 'bucket-433', 'is_public': True},
    {'bucket_name': 'bucket-602', 'is_public': True},
    {'bucket_name': 'bucket-547', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-433
# bucket-602
