# Day 1 - Exercise 38
# Context: Security Check. You must identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket_name-169', 'is_public': True},
    {'bucket_name': 'bucket_name-584', 'is_public': True},
    {'bucket_name': 'bucket_name-265', 'is_public': False},
    {'bucket_name': 'bucket_name-404', 'is_public': True},
    {'bucket_name': 'bucket_name-498', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:

