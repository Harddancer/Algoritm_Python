#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:46:39 2022

@author: yamamotod
"""


def removeDuplicates(nums) -> int:
      
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1 
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))