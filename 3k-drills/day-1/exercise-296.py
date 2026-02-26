# Day 1 - Exercise 296
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-890', 'is_public': False},
    {'bucket_name': 'bucket-522', 'is_public': False},
    {'bucket_name': 'bucket-972', 'is_public': False},
    {'bucket_name': 'bucket-967', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
