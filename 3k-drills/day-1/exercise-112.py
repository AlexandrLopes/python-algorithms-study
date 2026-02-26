# Day 1 - Exercise 112
# Context: Security Check. You must identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket_name-450', 'is_public': False},
    {'bucket_name': 'bucket_name-920', 'is_public': False},
    {'bucket_name': 'bucket_name-967', 'is_public': True},
    {'bucket_name': 'bucket_name-984', 'is_public': False},
    {'bucket_name': 'bucket_name-286', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:

