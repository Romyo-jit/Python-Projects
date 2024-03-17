#!/bin/env python
import random as rn
def coin():
    st=input('Press anything to flip a coin.')
    a=rn.randint(0,1)
    if a==1:
        print('Yes, Of Course.')
    else :
        print('Nah, Not A Chance.')
    coin()
coin()
