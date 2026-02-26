# Day 1 - Exercise 109
# Context: Security Check. You must identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket_name-361', 'is_public': False},
    {'bucket_name': 'bucket_name-414', 'is_public': False},
    {'bucket_name': 'bucket_name-719', 'is_public': True},
    {'bucket_name': 'bucket_name-789', 'is_public': False},
    {'bucket_name': 'bucket_name-352', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:

