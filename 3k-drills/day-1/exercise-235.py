# Day 1 - Exercise 235
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-935', 'is_public': True},
    {'bucket_name': 'bucket-965', 'is_public': True},
    {'bucket_name': 'bucket-138', 'is_public': True},
    {'bucket_name': 'bucket-238', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-935
# bucket-965
# bucket-138
