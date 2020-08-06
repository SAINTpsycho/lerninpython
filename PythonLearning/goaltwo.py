# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:10:30 2020

@author: varta
"""
import string

alpha_string = string.ascii_lowercase
alpha_list = list(alpha_string)
vowels = ['a', 'e', 'i', 'o', 'u']
name = 'mason grosko'


for x in alpha_list:
    if x in name:
        print(x.upper())
    else:
        if x in vowels:
            print(x.lower())