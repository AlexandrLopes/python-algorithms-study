# Day 1 - Exercise 266
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-458', 'is_public': True},
    {'bucket_name': 'bucket-956', 'is_public': True},
    {'bucket_name': 'bucket-303', 'is_public': False},
    {'bucket_name': 'bucket-187', 'is_public': False},
    {'bucket_name': 'bucket-394', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-458
# bucket-956
# bucket-394
