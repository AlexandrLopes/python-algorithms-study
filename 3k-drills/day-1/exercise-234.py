# Day 1 - Exercise 234
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-404', 'is_public': True},
    {'bucket_name': 'bucket-537', 'is_public': True},
    {'bucket_name': 'bucket-771', 'is_public': True},
    {'bucket_name': 'bucket-841', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:
for bucket in s3_buckets:
    if bucket["is_public"] == True:
        print(bucket["bucket_name"])


# -----------------------------------
# Expected Output:
# bucket-404
# bucket-537
# bucket-771
# bucket-841
