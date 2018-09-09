import subprocess
import os
pid_list =[x.split()[0] for x in subprocess.\
                run("ps x".split(),stdout=subprocess.PIPE).\
                stdout.decode('utf-8').rstrip().split("\n") if x.find("python mapper.py") >= 0]
for pid in pid_list:
    os.system(f"kill {pid}")