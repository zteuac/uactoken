import oci
import os
import requests
from oci.signer import Signer


lines = os.environ['PRIVATE_KEY'].split("\\n")
file = open("oci_api_key.pem", "w")
file.write('\n'.join(lines)+ '\n')
file.close()

auth = Signer(
    tenancy=os.environ['TENANCY_ID'],
    user=os.environ['USER'],
    fingerprint=os.environ['FINGURE'],
    private_key_file_location='oci_api_key.pem'
)
url = os.environ['URL']
# url = 'https://objectstorage.us-ashburn-1.oraclecloud.com/n/zte/b/artifacts-apps/o/cpu-load-0.0.1-SNAPSHOT.war'


local_filename = url.split('/')[-1]
r = requests.get(url, stream=True, auth=auth)
with open(local_filename, 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024): 
        if chunk:
            f.write(chunk)

os.remove("oci_api_key.pem")

##upload file to Object Storage Service via : oci os object put -ns zte  -bn artifacts-apps --name kubeconfig --file /home/daniel/.kube/config
