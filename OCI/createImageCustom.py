image_details = oci.core.models.CreateImageDetails(
    compartment_id='ocid1.compartment.oc1..xxxx',
    instance_id='ocid1.instance.oc1..xxxx',
    display_name='my_custom_image_2025-08-01'
)
response = compute.create_image(create_image_details=image_details)
print("Image OCID:", response.data.id)
