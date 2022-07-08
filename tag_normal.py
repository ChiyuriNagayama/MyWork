#!/usr/bin/env python
# coding: utf-8

# In[8]:


import random

def tag():
    tag = ["#work", "#experiment", "#room", "#home", "#walking", "#science", "#lifestyle", "#city", "#park"]
    return random.choice(tag)
title = tag()

def name():
    name = ["Nagayama Chiyuri", "Chiyuri Nagayama", "Nagayama Tiyuri", "Tiyuri Nagayama",
            "ちゆり", "ちゆりちゃん", "Chiyuri Tiyuri", "Tiyuri Chiyuri"]
    return random.choice(name)
meishi = name()

print(title, meishi)

def tag1():
    tag1 = ["chiyuri", "tiyuri", "nagayama", "chiyuri_tiyuri", "tiyuri_chiyuri"]
    return random.choice(tag1)
title1 = tag1()

def tag2():
    tag2 = ["知由理", "ちゆりん", "ちゆちゆ"]
    return random.choice(tag2)
title2 = tag2()

def tag3():
    tag3 = ["chiyuri_nagayama", "nagayama_chiyuri"]
    return random.choice(tag3)
title3 = tag3()

def tag4():
    tag4 = ["tiyuri_nagayama", "nagayama_tiyuri"]
    return random.choice(tag4)
title4 = tag4()

def tag5():
    tag5 = ["長山知由理", "長山ちゆり", "ながやまちゆり"]
    return random.choice(tag5)
title5 = tag5()

def tag6():
    tag6= ["ちゆり", "ちゆりちゃん"]
    return random.choice(tag6)
title6= tag6()

print(title1, title2, title3, title4, title5, title6)

def comment():
    comment = ["今日も元気です。", "今日も順調です。", "今日も楽しく過ごしています。"]
    return random.choice(comment)
subtitle = comment()

def name():
    name = ["長山 知由理", "長山 ちゆり", "ながやま ちゆり", "ちゆり", "ちゆりちゃん"]
    return random.choice(name)
meishi = name()

print(subtitle, "by", meishi)


# In[ ]:




