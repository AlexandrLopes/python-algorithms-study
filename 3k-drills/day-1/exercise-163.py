# Day 1 - Exercise 163
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-491', 'is_public': False},
    {'bucket_name': 'bucket-283', 'is_public': False},
    {'bucket_name': 'bucket-749', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-749
