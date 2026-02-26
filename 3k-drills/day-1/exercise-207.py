# Day 1 - Exercise 207
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-139', 'is_public': True},
    {'bucket_name': 'bucket-932', 'is_public': True},
    {'bucket_name': 'bucket-694', 'is_public': False},
    {'bucket_name': 'bucket-839', 'is_public': False},
    {'bucket_name': 'bucket-844', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-139
# bucket-932
# bucket-844
