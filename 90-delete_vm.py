import os
import subprocess

instance_names_list =[x.split()[0] for x in subprocess.\
                run("gcloud compute instances list".split(),stdout=subprocess.PIPE).\
                stdout.decode('utf-8').rstrip().split('\n')[1:]]

for instance_name in instance_names_list:
    command_list = [
        f"gcloud compute instances delete {instance_name} --delete-disks=all --quiet",
        f'sed -e "/{instance_name}/d" ~/.ssh/authorized_keys > tmp_keys',
        f"mv tmp_keys ~/.ssh/authorized_keys",
    ]
    for command in command_list:
        print(command)
        os.system(command)
    
