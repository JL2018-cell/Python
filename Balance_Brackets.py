# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:04:36 2021

@author: npatlj
"""


#Balance parenthesis, algorithm 1

s = "((()))(())(())()((())))))"
ls = []
state = 0

for i in range(len(s)):
    if len(ls)==0 and s[i]==")":
        print("Not balanced.")
        state = 1
        break
    if s[i]=="(":
        ls.append(s[i])
    if s[i]==")":
        if len(ls):
            ls.pop()
        else:
            print("Not balanced.")
            state = 1
            break

print(ls)
if not state:
    if len(ls)==0:
        print("Balanced.")
    else:
        print("Not balanced.")

    

    

