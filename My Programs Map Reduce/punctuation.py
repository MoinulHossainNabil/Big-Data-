#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:25:23 2019

@author: bjit-542
"""

from pyspark import *
import re
import string
from pyspark import SparkContext
sc=SparkContext.getOrCreate()
p=[]
path="/home/bjit-542/Big Data/input.txt"
with open(path, 'r') as myfile:
    data=myfile.read().replace('\n', '')
for d in data:
    if d in string.punctuation:
        p.append(d)
s='+'.join(p)
print(s)
output=open("/home/bjit-542/Big Data/punc.txt",'w')
output.write(s)
output.close()
text_file=sc.textFile("/home/bjit-542/Big Data/punc.txt")
punctuation=text_file.flatMap(lambda line: line.split("+"))
punctuation=punctuation.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
punctuation.saveAsTextFile("/home/bjit-542/Downloads/p")