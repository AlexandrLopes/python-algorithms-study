# Day 1 - Exercise 285
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-878', 'is_public': False},
    {'bucket_name': 'bucket-368', 'is_public': False},
    {'bucket_name': 'bucket-415', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-415
