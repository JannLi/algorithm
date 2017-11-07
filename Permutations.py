# -*- coding:utf-8 -*-

result = [] 
def perm(n,begin,end):  
    
    global result
    
    if begin == end:  
        print(n)  
    else:            
        for num in range(begin,end):  
            n[num],n[begin] = n[begin],n[num]  
            perm(n,begin+1,end)  
            n[num],n[begin] = n[begin],n[num]  
  
n=[1,2,3,4]  
perm(n,0,len(n)) 
 
        