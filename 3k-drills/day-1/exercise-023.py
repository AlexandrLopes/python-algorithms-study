# Day 1 - Exercise 23
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-423', 'is_public': True},
    {'bucket_name': 'bucket-397', 'is_public': True},
    {'bucket_name': 'bucket-176', 'is_public': True},
    {'bucket_name': 'bucket-825', 'is_public': True},
    {'bucket_name': 'bucket-695', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-423
# bucket-397
# bucket-176
# bucket-825
# bucket-695
