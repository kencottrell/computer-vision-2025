import oci

# Load config from the default location
config = oci.config.from_file()  # Optionally provide path/profile

# Create a Compute Client
compute_client = oci.core.ComputeClient(config)

# Replace this with your Compartment OCID
compartment_id = "ocid1.compartment.oc1..xxxx"

# List all compute instances in the compartment
response = compute_client.list_instances(compartment_id=compartment_id)

# Print out instance details
for instance in response.data:
    print(f"Name: {instance.display_name}, State: {instance.lifecycle_state}")
