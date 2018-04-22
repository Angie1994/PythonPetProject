import os
import string
import pprint
from collections import Counter

def wordsCount(List):
    SetTemp = set(List)
    print("all of the word count:")
    for elem in SetTemp:
        print("%20s : %d"%(elem, List.count(elem)))

def searchWordNum(List):
    char = input("input a str that you want to know it number:")
    print("The number of '%s' is %d." % (char, List.count(char)))

file_a = open("TEST2.txt", "rt")
str = file_a.read()
print(str)

#将该字符串中的所有不相关的字符用空格代替
for char in string.punctuation:
    str = str.replace(char, ' ')
print(str)

#将字符中的单词分割成列表
StrList = str.split()

#指定显示的单词
searchWordNum(StrList)

#打印出每一个单词出现的次数
wordsCount(StrList)

file_a.seek(0, os.SEEK_SET)
StrFile = file_a.read()
ReplaceWord = input("Input replace word:")
StrFile = StrFile.replace(ReplaceWord, '***')
print(StrFile)
#file_a.write(StrFile)  #再将输出值写入文件中
