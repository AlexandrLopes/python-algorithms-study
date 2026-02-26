# Day 1 - Exercise 182
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-844', 'is_public': True},
    {'bucket_name': 'bucket-162', 'is_public': False},
    {'bucket_name': 'bucket-192', 'is_public': False},
    {'bucket_name': 'bucket-653', 'is_public': False},
    {'bucket_name': 'bucket-467', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-844
# bucket-467
