#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:04:27 2022

@author: yamamotod
"""

"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""
import unittest

def natural(lists:int):
    s = 0
  
    for digit in range(1,abs(lists)+1):
            s += digit
            
    if s == round(lists*(lists+1)/2):
        print('ok')
        return ('OK')
    
        
    
natural(10)
        
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(('OK'), natural(5))
        self.assertEqual(('OK'), natural(4))
      
     
if __name__ == '__main__':
    unittest.main()