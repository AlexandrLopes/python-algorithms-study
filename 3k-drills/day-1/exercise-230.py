# Day 1 - Exercise 230
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-725', 'is_public': False},
    {'bucket_name': 'bucket-212', 'is_public': False},
    {'bucket_name': 'bucket-744', 'is_public': True},
    {'bucket_name': 'bucket-391', 'is_public': False},
    {'bucket_name': 'bucket-216', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-744
# bucket-216
