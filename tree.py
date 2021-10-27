# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:02:02 2021

@author: Tigran Boynagryan
"""

a = int(input())

for i in range(a):
    spaces = (a-(2*i+1))//2
    stars = 2*i+1
    print(" "*spaces,'*'*stars,' '*spaces)
    if stars == a:
        break
