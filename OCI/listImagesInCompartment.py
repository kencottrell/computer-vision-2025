import oci

config = oci.config.from_file()
compute = oci.core.ComputeClient(config)

images = compute.list_images(
    compartment_id='ocid1.compartment.oc1..xxxx',
    operating_system='Oracle Linux',
    operating_system_version='8',
    sort_by='TIMECREATED',
    sort_order='DESC'
).data

for image in images:
    print(f"Image: {image.display_name} - OCID: {image.id}")
