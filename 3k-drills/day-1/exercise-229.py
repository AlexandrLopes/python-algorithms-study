# Day 1 - Exercise 229
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-557', 'is_public': False},
    {'bucket_name': 'bucket-415', 'is_public': False},
    {'bucket_name': 'bucket-897', 'is_public': True},
    {'bucket_name': 'bucket-625', 'is_public': True},
    {'bucket_name': 'bucket-412', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-897
# bucket-625
