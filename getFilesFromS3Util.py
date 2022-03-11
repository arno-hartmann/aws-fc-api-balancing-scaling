import boto3

def getFilesFromS3 (bucketname):
   s3client = boto3.client('s3')

   response = s3client.list_objects(
      Bucket = bucketname
      )
   counter = 0
   for item in response["Contents"]:
      print(response["Contents"][counter]['Key'])
      counter +=1

