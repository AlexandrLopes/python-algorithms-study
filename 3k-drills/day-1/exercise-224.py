# Day 1 - Exercise 224
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-495', 'is_public': False},
    {'bucket_name': 'bucket-708', 'is_public': False},
    {'bucket_name': 'bucket-141', 'is_public': False},
    {'bucket_name': 'bucket-152', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-152
