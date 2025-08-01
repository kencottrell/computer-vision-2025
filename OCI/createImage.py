import oci

# Load config
config = oci.config.from_file()

# Create the Compute Client
compute_client = oci.core.ComputeClient(config)

# Set your compartment and instance OCID
compartment_id = "ocid1.compartment.oc1..xxxx"
instance_id = "ocid1.instance.oc1..xxxx"

# Image display name
display_name = "my_custom_image"

# Create the image
image_details = oci.core.models.CreateImageDetails(
    compartment_id=compartment_id,
    instance_id=instance_id,
    display_name=display_name
)

response = compute_client.create_image(create_image_details=image_details)
print("Image OCID:", response.data.id)
