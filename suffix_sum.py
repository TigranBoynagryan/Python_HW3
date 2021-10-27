# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:49:53 2021

@author: Tigran Boynagryan
"""

ls = [1.5,2.5,3]
ls1 = [1,2,3,4,5]

def suffix_sum(ls):
    sols = []
    for i in range(len(ls)):
        sols.append(sum(ls[i::]))

    return sols

print(suffix_sum(ls))
print(suffix_sum(ls1))