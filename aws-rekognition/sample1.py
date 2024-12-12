import boto3

STREAM_NAME = "your_stream_name"
kvs = boto3.client("kinesisvideo")
endpoint = kvs.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamName=STREAM_NAME
)['DataEndpoint']

kvam = boto3.client("kinesis-video-archived-media", endpoint_url=endpoint)
url = kvam.get_hls_streaming_session_url(StreamName=STREAM_NAME)['HLSStreamingSessionURL']
print(url)
