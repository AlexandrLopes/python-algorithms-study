# Day 1 - Exercise 90
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-393', 'is_public': False},
    {'bucket_name': 'bucket-655', 'is_public': True},
    {'bucket_name': 'bucket-353', 'is_public': False},
    {'bucket_name': 'bucket-349', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-655
