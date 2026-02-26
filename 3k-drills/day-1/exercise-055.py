# Day 1 - Exercise 55
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-140', 'is_public': True},
    {'bucket_name': 'bucket-216', 'is_public': False},
    {'bucket_name': 'bucket-112', 'is_public': False},
    {'bucket_name': 'bucket-310', 'is_public': False},
    {'bucket_name': 'bucket-242', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-140
