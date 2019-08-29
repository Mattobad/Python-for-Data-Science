# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:46:04 2019


String Manipulation examples

@author: s6040865
"""

test_str ="Hello, World"

print(test_str)

'''
indices
'''

print(test_str[0:-1])

'''
operator (Division)
6//3 int o/p
6/3 float o/p
'''


'''
Control structures

if, elif, else
while
break, continue, pass
'''
if 'e' in test_str:
    print('e is present in the string')
    
'''
Loops
'''
for ch in test_str:
    print(ch, end=' ')
    
print()

for ch in range(10):
    print(ch,end=' ')
    
 
    
    '''
    Assignment prime number
    NITIN.AKASH1989@GMAIL.COM
    SUBJECT: 5580:ACTIVITY1: SARBOTTAM THAPA MAGAR
    
    FOR AND IF TO CHECK THE NUMBER IS PRIME
    '''
    
    
'''
Tuple
 
'''
 

'''
Dictionary
'''

my_dict = {"list_item":{1,2,3}, "not_list":4}  
print(my_dict)
my_dict["new_item"] = "new value"
print(my_dict)


''''
sets
'''
x1={'foo','bar','baz'}
x2={'foo','bar','bue'}

print(x1.intersection(x2))
print(x1-x2)

print(x1.symmetric_difference)
    
print(x1.symmetric_difference_update)



'''
Modules

'''




