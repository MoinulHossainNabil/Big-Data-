from pyspark import *
import re

text_file=sc.textFile("/home/bjit-542/Big Data/input.txt")
#st=str(text_file)
s=text_file.flatMap(lambda line: re.split('[\.\?\!]', line)) #sentence count
w=text_file.flatMap(lambda line: re.split(r'[\.\?\!\s\_]', line)) #words count
s=s.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
w=w.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
s.saveAsTextFile("/home/bjit-542/Big Data/sentence.txt")
w.saveAsTextFile("/home/bjit-542/Big Data/words.txt")
