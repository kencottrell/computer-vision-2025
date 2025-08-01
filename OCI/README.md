# normally for linux: pip install oci
# but inside VS Code: 
py -m pip install <package>   -- this is the only command that works!!

# setup local config file
# Here’s a typical ~/.oci/config example snippet:


[DEFAULT]
user=ocid1.user.oc1..xxxx
fingerprint=xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx
key_file=/Users/you/.oci/oci_api_key.pem
tenancy=ocid1.tenancy.oc1..xxxx
region=us-ashburn-1