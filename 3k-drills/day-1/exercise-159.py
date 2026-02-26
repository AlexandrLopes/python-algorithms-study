# Day 1 - Exercise 159
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-455', 'is_public': False},
    {'bucket_name': 'bucket-199', 'is_public': True},
    {'bucket_name': 'bucket-788', 'is_public': False},
    {'bucket_name': 'bucket-496', 'is_public': False},
    {'bucket_name': 'bucket-401', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-199
# bucket-401
