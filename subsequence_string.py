# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 14:49:40 2021

@author: npatlj
"""

# Check if One String is a Subsequence of Another

def isSubSequence(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    index_str1 = 0  
    index_str2 = 0  
    # Traverse both str1 and str2
    while index_str1 < len_str1 and index_str2 < len_str2:
        # Compare current character of str2 with str1
        if str1[index_str1] == str2[index_str2]:
            # If matched, then move to next character in str1
            index_str1 = index_str1 + 1
        index_str2 = index_str2 + 1
    return index_str1 == len_str1


val_1 = 'abc'
val_2 = 'ahbgdc'
print(isSubSequence(val_1, val_2))