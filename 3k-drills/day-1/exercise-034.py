# Day 1 - Exercise 34
# Context: Security Check. You must identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket_name-307', 'is_public': False},
    {'bucket_name': 'bucket_name-256', 'is_public': True},
    {'bucket_name': 'bucket_name-553', 'is_public': True},
    {'bucket_name': 'bucket_name-931', 'is_public': False},
    {'bucket_name': 'bucket_name-918', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:

