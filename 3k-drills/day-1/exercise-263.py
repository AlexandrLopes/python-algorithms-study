# Day 1 - Exercise 263
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-924', 'is_public': False},
    {'bucket_name': 'bucket-587', 'is_public': False},
    {'bucket_name': 'bucket-782', 'is_public': False},
    {'bucket_name': 'bucket-150', 'is_public': True},
    {'bucket_name': 'bucket-177', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-150
# bucket-177
