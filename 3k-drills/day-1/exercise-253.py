# Day 1 - Exercise 253
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-662', 'is_public': True},
    {'bucket_name': 'bucket-399', 'is_public': False},
    {'bucket_name': 'bucket-405', 'is_public': True},
    {'bucket_name': 'bucket-285', 'is_public': False}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-662
# bucket-405
