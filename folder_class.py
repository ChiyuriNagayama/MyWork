#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import random
import shutil

tmp_path = input("ファイル格納先を選択してください。")
sep_num = int(input("何枚ずつに分割しますか？"))

path = tmp_path.replace(os.sep, "/")
flist = os.listdir(path)

file_list = []

for i in flist:
    file_list.append(i)
    
file_num = len(file_list) / sep_num

if (len(file_list) % sep_num) == 0:
    file_num2 = file_num
else:
    file_num2 = file_num + 1
              
rand_num = random.sample(range(100, 1000), int(file_num2))
tmp_num = input("採番を入力してください。")

num = 0

for i in range(0, len(rand_num)):
    for j in range(0, sep_num):
        os.makedirs(os.path.join(path, "{0:02d}".format(int(tmp_num)) + "_" + str(rand_num[i])), exist_ok = True) 
        
        if num + j == len(file_list):
            break

        move_from = path + "/" + file_list[num + j]
        move_to = os.path.join(path, "{0:02d}".format(int(tmp_num)) + "_" + str(rand_num[i]))
        shutil.move(move_from, move_to)
        
    num += sep_num
        


# In[ ]:




