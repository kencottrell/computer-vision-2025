import boto3
import sys
import importlib
import cv2
import os
import logging


from classes.RekognitionCollection import RekognitionCollection as rc
from  classes.RekognitionCollectionManager import RekognitionCollectionManager as rcm
from classes.RekognitionImage import RekognitionImage as ri
from classes.RekognitionFace import RekognitionFace as rf
from classes.RekognitionPerson import RekognitionPerson as rp

from pprint import pprint

from botocore.exceptions import ClientError

import requests

import json
#import time
import datetime

ct = datetime.datetime.now()
ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")
timestamp = int(round(ct.timestamp()))
logger = logging.getLogger(__name__)

 

debug = True
uploadtestfile = False



if debug:
    pprint('pprint: ' + str(pprint))
    print('boto3 client error: ' + ClientError.__name__)
    print('requests obj: ' + str(requests.__version__))
    print('json path: ' + str(json.__path__))
    # print('timenow / time obj: ' +str(timenow.__len__) + str(time.timezone))
    print("Current datetime: " +  str(timenow) +  " integer timestamp: " + str(timestamp))
    print('OS Path: ' + str(os.path))
    print('OpenCV version: ' + cv2.__version__)
    print('Logger info: ' + str(logger.level))
    print('=======Rekognition Objects==========')
    print('AWS rekognition Collection Mgr class: ' + str(rcm.__name__))
    print('AWS rekognition Collection  class: ' + str(rc.__name__))
    print('AWS rekognition image  class: ' + str(ri.__name__))
    print('AWS rekognition face  class: ' + str(rf.__name__))
    print('AWS rekognition person  class: ' + str(rp.__name__))


debug = False




def do_something():
    logger.info('Doing something')

sys.path.append('inputs')
sys.path.append('classes')
inputs_module = importlib.import_module('image-input-settings')


directory = 'C:\\Users\\kjcot\\mp4files\\'
file_name = "my_file.txt"

if not os.path.exists(directory):
    os.makedirs(directory)
s3testfilename = str(timestamp) + 'hello.txt'
file_path = os.path.join(directory, s3testfilename)

with open(file_path, "w") as f:
    f.write("This is the content of my file. " + "Current Time: " + str(timenow))




image_file_name = 'hotel-people.jpg'
image_file = inputs_module.inputdir + image_file_name
#  'manyfaces.jpg'
video_file_name = '3peoplewalking-vert.mp4'
# = '3peoplewalking-horiz.mp4'


region_name = 'us-east-2'
input_bucket = 'kens-input-files-bucket'

s3uri = 's3://' + input_bucket + '/' + image_file_name
arn = 'arn:aws:s3:::' + input_bucket + '/' + image_file_name
object_url = 'https://' + input_bucket+ '.s3.us-east-2.amazonaws.com/' + image_file_name



# 
# aws_access_key_id = ''     # UNUSED , makes use of AWS CLI, otherwise place value here
# aws_secret_access_key = ''   # makes use of AWS CLI creds, otherwise place value here
# rek = boto3.client('rekognition', 
#                           aws_access_key_id=aws_access_key_id,
#                           aws_secret_access_key=aws_secret_access_key,
#                            region_name='us-east-1')


s3 = boto3.client('s3', region_name=region_name)
rek = boto3.client('rekognition', region_name=region_name)
kvs = boto3.client("kinesisvideo", region_name=region_name )

if debug:
    print('rekognition Endpoint: ' + str(rek._endpoint))
    print('kinesis endpoint: ' + str(kvs._endpoint))
    print('s3 endpoint: ' + str(s3._endpoint))
    response = s3.list_objects(Bucket=input_bucket)

# test = ri(image_file, "testimage", rek)
testimage = ri.from_file(image_file, rek, "testimage2")
testcollectionmgr = rcm(rek)
testcollection = testcollectionmgr.create_collection("kens-example-collection2")
print(f"Created collection {testcollection.collection_id}:")
pprint(testcollection.describe_collection())


if uploadtestfile:
    s3.upload_file(file_path, input_bucket, s3testfilename)
    print(' source file read: ' + file_path)
    print(' uploaded to s3 as file name: ' + s3testfilename)
    uploadtestfile = False

def detect_faces(image_path):
    with open(image_path, 'rb') as image_file:
        response = rek.detect_faces(
            Image={'Bytes': image_file.read()},
            Attributes=['ALL']
        )
    return response



def compare_faces(bucket, source_file, target_file, region):
    client = boto3.client('rekognition', region_name=region)
    image_target = open(target_file, 'rb')
    response = client.compare_faces(
        SimilarityThreshold=99,
        SourceImage={'S3Object': {'Bucket': bucket, 'Name': source_file}},
        TargetImage={'Bytes': image_target.read()}
    )
    for face_match in response['FaceMatches']:
        position = face_match['Face']['BoundingBox']
        similarity = str(face_match['Similarity'])
        print(f"The face at {position['Left']} {position['Top']} matches with {similarity}% confidence")
    image_target.close()
    return len(response['FaceMatches'])

