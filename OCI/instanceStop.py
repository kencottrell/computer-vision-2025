import oci

# Load your OCI config from the default location (~/.oci/config)
config = oci.config.from_file()

# Create a Compute client
compute_client = oci.core.ComputeClient(config)

# Specify the OCID of the instance you want to stop
instance_id = "ocid1.instance.oc1..exampleuniqueid"

# Stop the instance
response = compute_client.instance_action(instance_id, "STOP")

print("Instance stop request sent. Work request ID:", response.headers.get('opc-work-request-id'))
