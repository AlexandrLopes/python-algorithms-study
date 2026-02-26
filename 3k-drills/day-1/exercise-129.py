# Day 1 - Exercise 129
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-619', 'is_public': True},
    {'bucket_name': 'bucket-594', 'is_public': False},
    {'bucket_name': 'bucket-227', 'is_public': False},
    {'bucket_name': 'bucket-322', 'is_public': False},
    {'bucket_name': 'bucket-649', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-619
# bucket-649
