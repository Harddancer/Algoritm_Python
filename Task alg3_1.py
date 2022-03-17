#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:37:53 2022

@author: yamamotod
"""


"""
В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
import unittest
def natural(a:int,b:int):
    m = []
    for i in range(a,b):
        for j in range(2,99):
            if j % i == 0:
                m.append(j)
                l = len(m)
            else:
                None
        print(f'Число {i} кратно/столько раз {l}')

natural(2,10)
"""
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(('Число', 2, 'кратно/столько раз', 49), natural(2,3))
       
      
     
      

if __name__ == '__main__':
    unittest.main()
"""