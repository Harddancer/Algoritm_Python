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

def natural(n:int):
    s = 0
  
    for i in range(1,abs(n)+1):
            s += i
            
    if s == round(n*(n+1)/2):
        print('ok')
        return ('OK')
    else:
        print('NOT ok')
        return ('NOT OK')
        
    
natural(10)
        
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(('OK'), natural(5))
        self.assertEqual(('OK'), natural(4))
      
     
if __name__ == '__main__':
    unittest.main()