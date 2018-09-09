
# coding: utf-8

# In[ ]:


import pathlib
import hashlib
import numpy as np
import pickle
import time
import random


# ## 自作MapReduce
# ### 課題
# ランダムで生成されたN個の整数(1<=, <=10000)の集合Aと  
# ランダムで生成されたM個の整数(1<=, <=10000)の集合Bの
# $$
# \sum_{a \in A, b \in B} a \cdot b
# $$
# を求める

# In[ ]:


def function(A, B):
    summed = 0
    for a in A:
        for b in B:
            summed += a*b
            
    return summed

while(True):
    source_list = list(pathlib.Path("source").glob("*"))
    for path in random.sample(source_list, len(source_list)):
        if str(path.name).startswith("."):
            continue
        target_fiile = pathlib.Path(f"target/{path.name}")
        if target_fiile.exists():
            continue
        with path.open("rb") as f:
            a, b = pickle.load(f)
        target_fiile.touch()
        print(a,b)
        target_value = function(a, b)
        with target_fiile.open("wb") as f:
            pickle.dump(target_value, f)
    time.sleep(1)

    

