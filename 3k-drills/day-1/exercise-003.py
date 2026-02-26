# Day 1 - Exercise 3
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-139', 'is_public': False},
    {'bucket_name': 'bucket-857', 'is_public': True},
    {'bucket_name': 'bucket-942', 'is_public': False},
    {'bucket_name': 'bucket-432', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-857
