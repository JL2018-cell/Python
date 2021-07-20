# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:32:04 2021

@author: npatlj
"""
#Balance parenthesis, algorithm 2

#s = "((()))(())(())()((())))))"
s = "()()()(()()()()()()()()()()()"
c = 0

for i in s:
    if i == "(":
        c += 1
    else:
        c -= 1
if c>0:
    print("Not balanced: Need exta",c,"left bracket \"(\"")
elif c<0:
    print("Not balanced: Need exta",-c,"right bracket \"(\"")
else:
    print("Balanced.")