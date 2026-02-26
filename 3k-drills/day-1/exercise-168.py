# Day 1 - Exercise 168
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-909', 'is_public': False},
    {'bucket_name': 'bucket-545', 'is_public': True},
    {'bucket_name': 'bucket-290', 'is_public': False},
    {'bucket_name': 'bucket-117', 'is_public': False},
    {'bucket_name': 'bucket-288', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-545
