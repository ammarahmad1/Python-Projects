# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 02:02:04 2021

@author: Ammar
"""
from collections import deque
stack = deque()
stack2 = deque()
word = input("Enter word : ")

for i in word:
    stack.append(i)
    
print(stack)

while len(stack) != 0:
   stack2.append(stack.pop())

print(stack2)

if(stack==stack2):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")


