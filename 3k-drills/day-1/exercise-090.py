# Day 1 - Exercise 90
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-393', 'is_public': False},
    {'bucket_name': 'bucket-655', 'is_public': True},
    {'bucket_name': 'bucket-353', 'is_public': False},
    {'bucket_name': 'bucket-349', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-655
