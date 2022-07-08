#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import random

tmp_path = input("ファイル格納先を選択してください。")

path = tmp_path.replace(os.sep, "/")
flist = os.listdir(path)

png_list = []

for i in flist:
    root, ext = os.path.splitext(i)
    if ext == ".png":
        png_list.append(i)
              
rand_num = random.sample(range(100, 1000), len(png_list))

i = 0

for png_file in png_list:
    num_i = "{0:04d}".format(rand_num[i])
    os.rename(os.path.join(path, png_file), os.path.join(path, num_i + "_" + png_file))
    i += 1

jpg_list = []

for j in flist:
    root, ext = os.path.splitext(j)
    if ext == ".jpg":
        jpg_list.append(j)
              
rand_num = random.sample(range(100, 1000), len(jpg_list))

j = 0

for jpg_file in jpg_list:
    num_j = "{0:04d}".format(rand_num[j])
    os.rename(os.path.join(path, jpg_file), os.path.join(path, num_j + "_" + jpg_file))
    j += 1


# In[ ]:




