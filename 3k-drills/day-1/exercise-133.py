# Day 1 - Exercise 133
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-156', 'is_public': False},
    {'bucket_name': 'bucket-888', 'is_public': True},
    {'bucket_name': 'bucket-369', 'is_public': True},
    {'bucket_name': 'bucket-865', 'is_public': True},
    {'bucket_name': 'bucket-285', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-888
# bucket-369
# bucket-865
# bucket-285
