# Day 1 - Exercise 240
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-150', 'is_public': False},
    {'bucket_name': 'bucket-728', 'is_public': True},
    {'bucket_name': 'bucket-102', 'is_public': True},
    {'bucket_name': 'bucket-473', 'is_public': False},
    {'bucket_name': 'bucket-562', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-728
# bucket-102
# bucket-562
