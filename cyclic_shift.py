# -*- ,coding: utf-8 -*-,
"""
Created on Wed Oct 27 19:06:18 2021

@author: Tigran Boynagryan
"""
N = int(input())
k = int(input())

def cyclic_shift(ls, N):
    x = ls[N - 1]
     
    for i in range(N - 1, 0, -1):
        ls[i] = ls[i - 1];
         
    ls[0] = x;
    return ls
 
ls = [int(i) for i in input() if i != ',']

i=0
while i<k:
    res  = cyclic_shift(ls, N)
    
    i+=1
    
print(res)

