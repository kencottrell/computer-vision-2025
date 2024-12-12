# pip install boto3

import boto3

def detect_faces(image_path):
    with open(image_path, 'rb') as image_file:
        response = rekognition.detect_faces(
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

# Example usage
bucket = 'bucket-name'
source_file = 'source-file-name'
target_file = 'target-file-name'
region = "region-name"
face_matches = compare_faces(bucket, source_file, target_file, region)
print(f"Face matches: {face_matches}")



rekognition = boto3.client('rekognition', 
                           aws_access_key_id='<YOUR_ACCESS_KEY>',
                           aws_secret_access_key='<YOUR_SECRET_KEY>',
                           region_name='us-east-1')
