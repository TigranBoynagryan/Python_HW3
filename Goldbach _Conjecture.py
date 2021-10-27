# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:03:28 2021

@author: Tigran Boynagryan
"""

n= int(input())

def prime_checker(n):
    indicator = 0
    isPrime = True
    if n==0 or n==1:
        isPrime=False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            indicator = 1
        else:
            continue
    if indicator == 1:
        isPrime = False
    

    return isPrime

primes = []
for i in range(n):
    if prime_checker(i):
        primes.append(i)
    else:
        continue
    
sol=[]
for i in primes:
    for j in primes:
        if i+j == n:
            a=[i,j]
            sol.append(a)
        else:
            continue
    if len(sol)==1:
         break
print([i for i in sol[0]])