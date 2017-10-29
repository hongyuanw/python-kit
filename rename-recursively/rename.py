#!/usr/bin/python
import os

for root, dirs, files in os.walk("/Users/yuanwhy/github/mage"):

    for oneDir in dirs :
        src = os.path.join(root, oneDir)
        dst = src.replace("yrpc", "mage")
        print src
        print dst
        os.rename(src, dst)
        
