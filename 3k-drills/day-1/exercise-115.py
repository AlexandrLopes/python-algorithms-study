# Day 1 - Exercise 115
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-709', 'is_public': True},
    {'bucket_name': 'bucket-684', 'is_public': True},
    {'bucket_name': 'bucket-360', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-709
# bucket-684
