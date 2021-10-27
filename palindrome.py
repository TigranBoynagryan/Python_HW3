# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:02:51 2021

@author: Tigran Boynagryan
"""

a = int(input())
b= int(input())

palindromes = []

for i in range(a,b+1):
    num = str(i)
    if num == num[::-1]:
        palindromes.append(int(num))
    else:
        continue
print(palindromes)