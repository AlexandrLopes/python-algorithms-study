# Day 1 - Exercise 238
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-875', 'is_public': True},
    {'bucket_name': 'bucket-436', 'is_public': True},
    {'bucket_name': 'bucket-776', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-875
# bucket-436
# bucket-776
