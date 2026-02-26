# Day 1 - Exercise 97
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-880', 'is_public': True},
    {'bucket_name': 'bucket-511', 'is_public': True},
    {'bucket_name': 'bucket-386', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-880
# bucket-511
