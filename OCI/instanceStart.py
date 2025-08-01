import oci

# Load your OCI config from default location (~/.oci/config)
config = oci.config.from_file()

# Create a Compute client
compute_client = oci.core.ComputeClient(config)

# Specify the OCID of the instance you want to start
instance_id = "ocid1.instance.oc1..exampleuniqueid"

# Start the instance
response = compute_client.instance_action(instance_id, "START")

print("Instance start request sent. Work request ID:", response.headers.get('opc-work-request-id'))
