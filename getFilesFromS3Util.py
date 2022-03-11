import boto3

def getFilesFromS3 (bucketname):
   s3client = boto3.client('s3')
#   print(s3client)
#   print(type(s3client))

   response = s3client.list_objects(
      Bucket = bucketname
      )
   print(response["Contents"][0]['Key'])

