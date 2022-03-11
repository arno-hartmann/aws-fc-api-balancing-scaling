import boto3
import json
import os


def getFilesFromS3 (bucketname):
   s3client = boto3.client('s3')

   response_list = s3client.list_objects(
      Bucket = bucketname
      )

   answer_array = []
   for item in response_list["Contents"]:

      key = item['Key']
      response_content = s3client.get_object(
         Bucket = bucketname,
         Key = key
         )

      text = response_content['Body'].read()
      
      words = text.split()
      numberOfWords = len(words)
   
      #message = 'Number of words in text file {} is {}'.format(key, numberOfWords)
      #print(message)

      answer_object = {"key" : key, "words" : numberOfWords}
      answer_array.append(answer_object)
     
   print("-----------")
   print(answer_array)
   return answer_array 