# Day 1 - Exercise 122
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-693', 'is_public': False},
    {'bucket_name': 'bucket-324', 'is_public': True},
    {'bucket_name': 'bucket-888', 'is_public': True},
    {'bucket_name': 'bucket-948', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucketname"])



# -----------------------------------
# Expected Output:
# bucket-324
# bucket-888
# bucket-948
