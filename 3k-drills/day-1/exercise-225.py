# Day 1 - Exercise 225
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-577', 'is_public': True},
    {'bucket_name': 'bucket-868', 'is_public': True},
    {'bucket_name': 'bucket-385', 'is_public': True},
    {'bucket_name': 'bucket-786', 'is_public': True},
    {'bucket_name': 'bucket-605', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-577
# bucket-868
# bucket-385
# bucket-786
