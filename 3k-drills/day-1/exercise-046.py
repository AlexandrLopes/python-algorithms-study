# Day 1 - Exercise 46
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-768', 'is_public': True},
    {'bucket_name': 'bucket-240', 'is_public': False},
    {'bucket_name': 'bucket-339', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-768
# bucket-339
