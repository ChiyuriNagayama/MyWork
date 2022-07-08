#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import random

tmp_path = input("ファイル格納先を選択してください。")

path = tmp_path.replace(os.sep, "/")
flist = os.listdir(path)

gif_list = []

for i in flist:
    root, ext = os.path.splitext(i)
    if ext == ".gif":
        gif_list.append(i)
              
rand_num = random.sample(range(100, 1000), len(gif_list))

i = 0

for gif_file in gif_list:
    num_i = "{0:04d}".format(rand_num[i])
    os.rename(os.path.join(path, gif_file), os.path.join(path, num_i + "_" + gif_file))
    i += 1


# In[ ]:




