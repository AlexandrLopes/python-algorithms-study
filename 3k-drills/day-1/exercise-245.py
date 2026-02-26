# Day 1 - Exercise 245
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-352', 'is_public': True},
    {'bucket_name': 'bucket-326', 'is_public': True},
    {'bucket_name': 'bucket-309', 'is_public': True},
    {'bucket_name': 'bucket-184', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-352
# bucket-326
# bucket-309
# bucket-184
