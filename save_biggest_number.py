# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 14:28:49 2017

@author: JANN
"""
string = "9981532941"
n = 6
left = len(string)-n
array=[]
for j in string:
    array.append(j)
array1 = map(int,array)

i = 0
result = ""
while i<left:   
    if len(array1) == left-i:
        for l in array1:
            result += str(l)
        break

    else:
        maximum = max(array1[:len(array1)-left+i+1])
        idx = array1.index(maximum)
        result += str(maximum)
        array1 = array1[idx+1:]
        i += 1
print(result)
