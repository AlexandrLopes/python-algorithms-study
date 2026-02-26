# Day 1 - Exercise 197
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-996', 'is_public': True},
    {'bucket_name': 'bucket-250', 'is_public': True},
    {'bucket_name': 'bucket-380', 'is_public': False},
    {'bucket_name': 'bucket-482', 'is_public': False},
    {'bucket_name': 'bucket-522', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-996
# bucket-250
# bucket-522
