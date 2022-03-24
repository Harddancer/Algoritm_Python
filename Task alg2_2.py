#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:03:31 2022

@author: yamamotod
"""
import unittest

def desc_number(number:int):
    result=0
    while number > 0:
        digit = number % 10
        number = number // 10
        result = result * 10
        result = result + digit 
 
    print(f'Обратка:, {result}')
    return result   



class Test_n(unittest.TestCase):
    def test_n(self):
        self.assertEqual((321), desc_number(123))
        self.assertEqual((987654321), desc_number(123456789))
      
     
      

if __name__ == '__main__':
    unittest.main()