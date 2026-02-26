# Day 1 - Exercise 258
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-145', 'is_public': False},
    {'bucket_name': 'bucket-843', 'is_public': True},
    {'bucket_name': 'bucket-619', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-843
# bucket-619
