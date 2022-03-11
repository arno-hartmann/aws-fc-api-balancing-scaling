import json
import boto3
import os



def getFilesFromS3 (bucketname):
   s3client = boto3.client('s3')

   key = s3client['Records'][0]['s3']['object']['key']

   response = s3client.get_object(
      Bucket = bucket,
      Key = key
      )
   
   text = response['Body'].read()

   words = text.split()
   numberOfWords = len(words)
   
   message = 'Number of words in text file {} is {}'.format(key, numberOfWords)
   
   print(message)