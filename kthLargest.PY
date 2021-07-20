# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:07:45 2021

@author: npatlj
"""

import bisect
# Find the k-th Largest Element in an Unsorted Array

def find_k_largest_element(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k-1]

def find_k_largest_element2(nums, k):
    for i in range(k-1):
        nums.remove(max(nums))
    return max(nums)

def find_k_largest_element3(nums, k):
    n = len(nums)
    if k > math.log(n, 2):
        return find_k_largest_element(nums, k)
    else:
        return find_k_largest_element2(nums, k)
    
def find_k_largest_element4(nums, k):
    tmp = []
    for i in range(k):
        tmp.append(nums[i])
    tmp.sort()
    for i in range(k, len(nums)):
        if nums[i] > tmp[len(tmp)-1]:
            tmp = tmp[1:len(tmp)]
            tmp.append(nums[i])
            tmp.sort()
    return tmp[0]

def find_k_largest_element5(nums, k):
    window = nums[:k]
    for element in nums[k:]:
        if element > window[0]:
            # Remove minimum from window
            window = window[1:]

            # Sorted insert of new element
            bisect.insort(window, element)
    return window[0]

ls = [1,2,3,4,5,6,7,8,9,10,11]
print(find_k_largest_element4(ls,2))
        