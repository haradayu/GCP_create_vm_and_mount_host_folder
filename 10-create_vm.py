import os

machine_type = 'f1-micro'
image = "conda3ml"


for i in range(1):
    instance_name = f"instance-{i}"
    #command = f"gcloud compute instances create {instance_name} --preemptible --machine-type {machine_type} --image {image}"
    command = f"gcloud compute instances create {instance_name} --preemptible --image {image} --custom-cpu 8 --custom-memory 7424MB"
    print(command)
    os.system(command)
    
