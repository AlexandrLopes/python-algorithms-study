# Day 1 - Exercise 155
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-664', 'is_public': False},
    {'bucket_name': 'bucket-935', 'is_public': False},
    {'bucket_name': 'bucket-492', 'is_public': True},
    {'bucket_name': 'bucket-636', 'is_public': True},
    {'bucket_name': 'bucket-465', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-492
# bucket-636
# bucket-465
