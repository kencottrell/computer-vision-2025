import oci

# Load your OCI CLI config
config = oci.config.from_file()

# Initialize the Compute client
compute_client = oci.core.ComputeClient(config)

# Define variables - change these values to your actual ones
image_id = 'ocid1.image.oc1..exampleuniqueID'  # OCID of the image to export
namespace = 'your_namespace'                   # Object Storage namespace in OCI
bucket_name = 'your_bucket'                     # Bucket name
object_name = 'exported_image.qcow2'            # Exported image file name
region = config['region']                        # Region from your config

# Construct the Object Storage URL for export (format: https://objectstorage.<region>.oraclecloud.com/n/<namespace>/b/<bucket>/o/<object>)
object_storage_url = (
    f"https://objectstorage.{region}.oraclecloud.com/n/{namespace}/b/{bucket_name}/o/{object_name}"
)

# Create ExportImageViaObjectStorageUriDetails with destination URL and export format
export_details = oci.core.models.ExportImageViaObjectStorageUriDetails(
    destination_type="objectStorageUri",
    destination_uri=object_storage_url,
    export_format="QCOW2"  # Other formats: OCI, VMDK, VHD, VDI
)

# Call export_image API
response = compute_client.export_image(
    image_id=image_id,
    export_image_details=export_details
)

print(f"Export initiated. Work request ID: {response.headers['opc-work-request-id']}")
