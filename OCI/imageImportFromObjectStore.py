from oci.core.models import CreateImageDetails, ImageSourceViaObjectStorageTupleDetails

image_source = ImageSourceViaObjectStorageTupleDetails(
    bucket_name="your_bucket",
    namespace_name="your_namespace",
    object_name="your-image-file.qcow2",
    source_image_type="QCOW2"
)

image_details = CreateImageDetails(
    compartment_id=compartment_id,
    image_source_details=image_source,
    display_name="imported_image"
)

response = compute_client.create_image(create_image_details=image_details)
print("Imported Image OCID:", response.data.id)
