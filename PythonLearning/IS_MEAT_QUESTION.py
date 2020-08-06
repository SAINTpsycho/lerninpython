# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:34:50 2020

@author: varta
"""

'''fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit.capitalize())    
[fruit.capitalize() for fruit in fruits]'''

''' 
GOAL: PRINT OUT UPPER CASED VEGETABLES
AND LOWER CASED FRUITS FROM THE FOODS LIST
AND TITLED ITEMS THAT ARE BOTH FRUITS AND VEGGIES
AND YELL "THAT'S NOT A FOOD" IF NOT A FOOD
'''

potential_foods = [
    'apple', 'asparagus', 'strawberry', 'cherry', 'bacon', 'tomato',
    'motor oil', 'surstromming', 'STEAK', 'hamburger'
]
fruits = ['apple', 'orange', 'strawberry', 'cherry', 'tomato']
veggies = ['corn', 'asparagus', 'broccoli', 'green bean', 'tomato']
meats = ['BACON', 'steak', 'Ham Burger']
foods = fruits + veggies + meats

for x in potential_foods:
    if x in veggies:
        if x in fruits:
            print(x.title())
        else:
            print(x.upper())
    elif (x in fruits) and (x not in veggies):
        print(x)    
        
    elif (x.upper() not in foods) and (x.lower() not in foods) and (x not in [y.replace(" ","").lower() for y in foods]):
        print(x, "THAT IS NOT A FOOD!!!")
   
    else:
        print(x, "THAT IS A MEAT")