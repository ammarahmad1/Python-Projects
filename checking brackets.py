# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 02:14:38 2021

@author: Ammar
"""
from collections import deque

sobrackets = deque()
scbrackets = deque()
cobrackets = deque()
ccbrackets = deque()
pobrackets = deque()
pcbrackets = deque()


object = input("Enter your sentence ")

for i in object:
    if(i == '[' ):
        sobrackets.append(i)
    elif(i == ']' ):
        scbrackets.append(i)
    if(i == '{' ):
        cobrackets.append(i)
    elif(i == '}' ):
        ccbrackets.append(i)
    if(i == '(' ):
        pobrackets.append(i)
    elif(i == ')' ):
        pcbrackets.append(i)
    
print(pobrackets)
print(pcbrackets)

if (sobrackets == scbrackets):
    print("square brackets are equal")
else:
    print("square brackets are not equal")
if (cobrackets == ccbrackets):
    print("Curly brackets are equal")
else:
    print("Curly brackets are not equal")
if (pobrackets == pcbrackets):
    print("Parenthesis brackets are equal")
else:
    print("Parenthesis brackets are not equal")
