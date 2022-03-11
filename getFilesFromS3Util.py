import boto3
import json
import os


def getFilesFromS3 (bucketname):
   s3client = boto3.client('s3')

   response_list = s3client.list_objects(
      Bucket = bucketname
      )


   counter = 0
   for item in response_list["Contents"]:

      key = response_list["Contents"][counter]['Key']
      
      response_content = s3client.get_object(
         Bucket = bucketname,
         Key = key
         )

      text = response_content['Body'].read()
      
      words = text.split()
      numberOfWords = len(words)
   
      #message = 'Number of words in text file {} is {}'.format(key, numberOfWords)
      #print(message)

      answer_array = [counter, "\"key\" :", key, "\"words\":", numberOfWords ]
      print(answer_array)
      counter +=1
      return answer_array