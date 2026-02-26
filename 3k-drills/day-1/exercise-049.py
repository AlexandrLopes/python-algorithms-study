# Day 1 - Exercise 49
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-149', 'is_public': True},
    {'bucket_name': 'bucket-269', 'is_public': True},
    {'bucket_name': 'bucket-544', 'is_public': True},
    {'bucket_name': 'bucket-776', 'is_public': False},
    {'bucket_name': 'bucket-749', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-149
# bucket-269
# bucket-544
# bucket-749
