# Day 1 - Exercise 73
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-632', 'is_public': False},
    {'bucket_name': 'bucket-773', 'is_public': True},
    {'bucket_name': 'bucket-169', 'is_public': False},
    {'bucket_name': 'bucket-888', 'is_public': False},
    {'bucket_name': 'bucket-663', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-773
