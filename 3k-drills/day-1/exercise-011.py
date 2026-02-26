# Day 1 - Exercise 11
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-286', 'is_public': True},
    {'bucket_name': 'bucket-228', 'is_public': False},
    {'bucket_name': 'bucket-413', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-286
# bucket-413
