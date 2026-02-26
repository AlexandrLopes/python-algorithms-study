# Day 1 - Exercise 248
# Context: Security Check. Identify S3 buckets exposed to the public.

s3_buckets = [
    {'bucket_name': 'bucket-567', 'is_public': False},
    {'bucket_name': 'bucket-160', 'is_public': False},
    {'bucket_name': 'bucket-697', 'is_public': True},
    {'bucket_name': 'bucket-601', 'is_public': True},
    {'bucket_name': 'bucket-480', 'is_public': True}
]

# TODO: Write a for loop to print the 'bucket_name' ONLY if 'is_public' is True.
# Write your code below:



# -----------------------------------
# Expected Output:
# bucket-697
# bucket-601
# bucket-480
