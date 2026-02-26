# Day 1 - Exercise 70
# Context: Security Check. You must identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket_name-828', 'is_public': False},
    {'bucket_name': 'bucket_name-307', 'is_public': False},
    {'bucket_name': 'bucket_name-697', 'is_public': True},
    {'bucket_name': 'bucket_name-524', 'is_public': False},
    {'bucket_name': 'bucket_name-643', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:

