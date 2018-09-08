import os
import subprocess
instance_names =[x.split()[0]  for x in subprocess.\
                run("gcloud compute instances list".split(),stdout=subprocess.PIPE).\
                stdout.decode('utf-8').rstrip().split('\n')[1:] if x.split()[-1] == "RUNNING"]
print(instance_names)

USER_NAME = os.environ["USER_NAME"]
HOST_IP = os.environ["HOST_IP"]

for instance_name in instance_names:
    commands_list = [
        f'ifconfig',
    ]
    for cmd in commands_list:
        gcloud_plus_cmd = f'gcloud compute ssh {USER_NAME}@{instance_name} --command "{cmd}"'
        print(gcloud_plus_cmd)
        os.system(gcloud_plus_cmd)