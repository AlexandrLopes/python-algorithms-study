# Day 1 - Exercise 107
# Context: Security Check. You must identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket_name-333', 'is_public': False},
    {'bucket_name': 'bucket_name-429', 'is_public': False},
    {'bucket_name': 'bucket_name-549', 'is_public': True},
    {'bucket_name': 'bucket_name-677', 'is_public': True},
    {'bucket_name': 'bucket_name-239', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:

