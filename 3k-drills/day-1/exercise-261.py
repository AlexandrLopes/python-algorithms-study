# Day 1 - Exercise 261
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-745', 'is_public': False},
    {'bucket_name': 'bucket-966', 'is_public': True},
    {'bucket_name': 'bucket-357', 'is_public': True},
    {'bucket_name': 'bucket-142', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-966
# bucket-357
# bucket-142
