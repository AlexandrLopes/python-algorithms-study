# Day 1 - Exercise 280
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-308', 'is_public': False},
    {'bucket_name': 'bucket-988', 'is_public': True},
    {'bucket_name': 'bucket-862', 'is_public': False},
    {'bucket_name': 'bucket-657', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-988
