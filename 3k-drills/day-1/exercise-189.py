# Day 1 - Exercise 189
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-458', 'is_public': False},
    {'bucket_name': 'bucket-212', 'is_public': False},
    {'bucket_name': 'bucket-358', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# (No output expected for this specific random data)
