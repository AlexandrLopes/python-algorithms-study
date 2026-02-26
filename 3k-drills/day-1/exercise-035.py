# Day 1 - Exercise 35
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-126', 'is_public': False},
    {'bucket_name': 'bucket-161', 'is_public': True},
    {'bucket_name': 'bucket-802', 'is_public': True},
    {'bucket_name': 'bucket-558', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-161
# bucket-802
# bucket-558
