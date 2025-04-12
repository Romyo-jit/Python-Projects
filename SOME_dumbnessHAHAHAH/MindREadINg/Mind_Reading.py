
#Completed

from random import randint
from COOLEST_thing.dotmodule import Dot
import sys

def val(num):
    if num=='e':
        sys.exit()

def start():
        rand=randint(2,20)
        if rand%2==0:
            print("Let's play a game. I am about to read your mind.\nYou can anytime enter 'e' to exit.")
            o=input("1. Think of a number. Remember it for the rest of time. Press any key to continue.")
            val(o)
            c=input("2. Multiply the number by 2. Press any key to continue.")
            val(c)
            m=rand/2
            value=str(rand)
            b=input("3. Add "+value+" to the value. Press any key to continue.")
            val(b)
            d=input("4. Now devide the number by 2. Press any key to continue.")
            val(d)
            f=input("5. At last substract the value to the number you thought at first. Press any key to continue.")
            val(f)
            m=str(m)
            print("\n\nI am about to read your mind", end = "")
            Dot(8)
            print("\n\nYou are thinking of--- "+m+"\n"+7*"^--^--"+rand*"\n")
            en=input("\nDo you want to play again ?('y' or 'n'): ")
            if en=='y':
                start()
            else:
                val('e')
        else:
            start()

start()