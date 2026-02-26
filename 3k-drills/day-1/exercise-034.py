# Day 1 - Exercise 34
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-625', 'is_public': True},
    {'bucket_name': 'bucket-409', 'is_public': True},
    {'bucket_name': 'bucket-626', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-625
# bucket-409
# bucket-626
