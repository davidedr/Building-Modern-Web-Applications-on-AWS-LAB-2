import boto3
import json

S3API = boto3.client("s3", region_name="us-west-2") 
bucket_name = "c11284a122552l656969t1w707241354095-s3bucket-1wgn8jpz9rblb"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")