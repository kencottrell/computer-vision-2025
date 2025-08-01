import oci

# Load OCI config
config = oci.config.from_file()  # Uses default profile and config file

# Create Compute client
compute_client = oci.core.ComputeClient(config)

# Define your variables
compartment_id = "ocid1.compartment.oc1..exampleuniqueid"
availability_domain = "your-availability-domain"  # e.g., "Uocm:PHX-AD-1"
shape = "VM.Standard2.1"  # shape of the instance
image_id = "ocid1.image.oc1..exampleuniqueimageid"  # OCID of the source image
subnet_id = "ocid1.subnet.oc1..examplesubnetid"  # subnet for the VNIC

# Specify the source image
instance_source = oci.core.models.InstanceSourceViaImageDetails(image_id=image_id)

# Configure VNIC for network
create_vnic_details = oci.core.models.CreateVnicDetails(subnet_id=subnet_id)

# Prepare the launch details
launch_details = oci.core.models.LaunchInstanceDetails(
    display_name="My New Instance",
    compartment_id=compartment_id,
    availability_domain=availability_domain,
    shape=shape,
    source_details=instance_source,
    create_vnic_details=create_vnic_details,
    metadata={"ssh_authorized_keys": "ssh-rsa AAAAB3... your public ssh key ..."},
)

# Launch the instance
response = compute_client.launch_instance(launch_details)

print("Instance launched. OCID:", response.data.id)
