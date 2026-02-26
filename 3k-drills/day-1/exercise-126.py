# Day 1 - Exercise 126
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-640', 'is_public': False},
    {'bucket_name': 'bucket-721', 'is_public': False},
    {'bucket_name': 'bucket-494', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-494
