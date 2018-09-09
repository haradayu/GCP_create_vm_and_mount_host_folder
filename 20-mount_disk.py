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
        f'gcloud compute ssh {USER_NAME}@{instance_name} --command "ssh-keygen -N  \'\' -f ~/.ssh/id_rsa"', \
        f'gcloud compute ssh {USER_NAME}@{instance_name}  --command "cat ~/.ssh/id_rsa.pub" >> ~/.ssh/authorized_keys', \
        f'gcloud compute ssh {USER_NAME}@{instance_name}  --command "mkdir /home/{USER_NAME}/conoha"', \
        f'gcloud compute ssh {USER_NAME}@{instance_name} --command "sshfs {USER_NAME}@{HOST_IP}:/home/{USER_NAME}/ /home/{USER_NAME}/conoha -p 55959 -oStrictHostKeyChecking=no"',
    ]
    for cmd in commands_list:
        print(cmd)
        os.system(cmd)