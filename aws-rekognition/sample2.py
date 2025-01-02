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
import time
import datetime

ct = datetime.datetime.now()
ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")
ts = ct.time

debug = True



if debug:
    pprint('pprint: ' + str(pprint))
    print('boto3 client error: ' + ClientError.__name__)
    print('requests obj: ' + str(requests.__version__))
    print('json path: ' + str(json.__path__))
    print('timenow / time obj: ' +str(timenow.__len__) + str(time.timezone))
    print('AWS rekognition Collection Mgr class: ' + str(rcm.__name__))
    print('AWS rekognition Collection  class: ' + str(rc.__name__))
    print('AWS rekognition image  class: ' + str(ri.__name__))
    print('AWS rekognition face  class: ' + str(rf.__name__))
    print('AWS rekognition person  class: ' + str(rp.__name__))


debug = False


print('OS Path: ' + str(os.path))
print('OpenCV version: ' + cv2.__version__)
logger = logging.getLogger(__name__)
print('Logger info: ' + str(logger.level))

def do_something():
    logger.info('Doing something')

sys.path.append('inputs')
sys.path.append('classes')
inputs_module = importlib.import_module('video-inout-settings')
inputs_module = importlib.import_module('classes')



upload_test_file = 'C:\\Users\\kjcot\\mp4files\\testfile.txt'


image_file = 'hotel-people.jpg'
#image_file = 'manyfaces.jpg'
video_file = '3peoplewalking-vert.mp4'
#video_file = '3peoplewalking-horiz.mp4'

region_name = 'us-east-2'
input_bucket = 'kens-input-files-bucket'

s3uri = 's3://' + input_bucket + '/' + image_file
arn = 'arn:aws:s3:::' + input_bucket + '/' + image_file
object_url = 'https://' + input_bucket+ '.s3.us-east-2.amazonaws.com/' + image_file


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

test = ri(image_file, "testimage", rek)

s3testfilename = str(ts) + 'hello.txt'
s3.upload_file(upload_test_file, input_bucket, s3testfilename)

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

