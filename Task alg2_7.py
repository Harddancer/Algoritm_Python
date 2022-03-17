#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:49:48 2022

@author: yamamotod
"""
"""
Write a function that reverses a string. 
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory
"""
import unittest

class Solution:
    def reverseString(self, s:list) -> None:
        if len(s) == 1:
            return s
        return s[-1] + self.reverseString(s[:-1])
    
    def __str__(self):
        return str(self.__class__)# не могу понять как вернуть print  объекта
     

class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
       cls.n = Solution()
       cls.n1 = Solution()
       
     
    def test(self):
        
        self.assertEqual(self.n.reverseString('54321'), '12345')
        self.assertEqual(self.n1.reverseString('123'), '321')
        
     
if __name__ == '__main__':
    unittest.main()        
        
      
        
        



