To use AWS Rekognition with an RTSP input, follow these steps:
Set Up Kinesis Video Streams: Use Amazon Kinesis Video Streams to ingest live video from an RTSP camera. You can use a Raspberry Pi or similar device to stream the RTSP feed to Kinesis Video Streams1
8.
Configure the Stream: Set up the necessary AWS IoT credentials and IAM roles to securely connect and stream video to Kinesis89.
Create a Stream Processor: Use AWS Rekognition Video to create a stream processor that analyzes the video stream for specific labels or faces511.
Process and Analyze: The stream processor will analyze the video in real-time, and results can be sent to an S3 bucket or an SNS topic for further action3