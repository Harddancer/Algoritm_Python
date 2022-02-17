#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:35:51 2022

@author: yamamotod
"""
"""
Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 
...Количество элементов (n) вводится с клавиатуры.
"""
import unittest
def element(n:int):
    #n = int(input('Введите количество элементов: '))
    i = 0
    number = 1
    summa = 0
    while i < n:
        summa += number
        number /= -2
        
        i += 1

    print(f'Сумма {summa}')
    return summa



class Test_n(unittest.TestCase):
    def test_n(self):
        self.assertEqual((0.6875), element(5))
        self.assertEqual((0.625), element(4))
      
     
      

if __name__ == '__main__':
    unittest.main()