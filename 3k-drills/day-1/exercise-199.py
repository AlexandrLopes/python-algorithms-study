# Day 1 - Exercise 199
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-464', 'is_public': True},
    {'bucket_name': 'bucket-206', 'is_public': True},
    {'bucket_name': 'bucket-350', 'is_public': True},
    {'bucket_name': 'bucket-247', 'is_public': False},
    {'bucket_name': 'bucket-269', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-464
# bucket-206
# bucket-350
