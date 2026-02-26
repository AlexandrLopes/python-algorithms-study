# Day 1 - Exercise 87
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-862', 'is_public': False},
    {'bucket_name': 'bucket-543', 'is_public': False},
    {'bucket_name': 'bucket-357', 'is_public': False},
    {'bucket_name': 'bucket-119', 'is_public': False},
    {'bucket_name': 'bucket-826', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"]:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-826
