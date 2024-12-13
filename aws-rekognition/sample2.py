import boto3
import sys
import importlib
import cv2
import os
print(os.path)
print(cv2.__version__)

sys.path.append('inputs')
inputs_module = importlib.import_module('video-inout-settings')
classes_module = importlib.import_module('classes')

debug = True
aws_access_key_id = ''
aws_secret_access_key = ''
if debug:
    rek = boto3.client('rekognition', region_name="us-east-1")
else:
    rek2 = boto3.client('rekognition', 
                           aws_access_key_id=aws_access_key_id,
                           aws_secret_access_key=aws_secret_access_key,
                           region_name='us-east-1')

kvs = boto3.client("kinesisvideo", region_name="us-east-1" )


print('rekognition Endpoint: ' + str(rek._endpoint))
print('kinesis endpoint: ' + str(kvs._endpoint))


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



