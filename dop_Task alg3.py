#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:48:36 2022

@author: yamamotod
"""
"""
Contains Duplicate
Given an integer array nums, return true if any value appears
at least twice in the array, 
and return false if every element is distinct
"""

class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
test = Solution()
print(test.containsDuplicate([1,1,2,3,4,5]))
print(test.containsDuplicate([1,2,3,4,5]))