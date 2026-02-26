# Day 1 - Exercise 217
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-531', 'is_public': False},
    {'bucket_name': 'bucket-443', 'is_public': False},
    {'bucket_name': 'bucket-565', 'is_public': True},
    {'bucket_name': 'bucket-135', 'is_public': False},
    {'bucket_name': 'bucket-189', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-565
