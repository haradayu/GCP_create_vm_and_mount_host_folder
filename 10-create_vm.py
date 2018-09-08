import os

machine_type = 'f1-micro'
image = "conda3ml"


for i in range(2):
    instance_name = f"instance-{i}"
    command = f"gcloud compute instances create {instance_name} --preemptible --machine-type {machine_type}\
                --image {image}"
    print(command)
    os.system(command)
    
