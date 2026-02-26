# Day 1 - Exercise 9
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-338', 'is_public': False},
    {'bucket_name': 'bucket-989', 'is_public': True},
    {'bucket_name': 'bucket-492', 'is_public': False},
    {'bucket_name': 'bucket-706', 'is_public': False},
    {'bucket_name': 'bucket-212', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-989
