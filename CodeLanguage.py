# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

#####COMPLETED#####

from random import randrange as rn
from time import sleep
from dotmodule import Dot

letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

def ran3():
    emp=''
    for i in range(0,3):
        num=rn(0,len(letters))
        emp=emp+letters[num]
    return emp

def EsentenceSpilt(strin):
    ens=''
    spi=strin.split(' ')
    for i in range(0,len(spi)):
        ens=ens+encrypt(spi[i])+' '
    return ens

def DsentenceSpilt(strin):
    des=''
    spi=strin.split(' ')
    for i in range(0,len(spi)):
        des=des+decrypt(spi[i])+' '
    return des

def encrypt(strin):
    list1=[]
    temp=''
    if len(strin)<=3:
        for i in range (0,len(strin)):
            temp=strin[i]+temp
        return temp
    for i in range(0,len(strin)):
        list1.append(strin[i])
    pick=list1.pop(0)
    list1.insert(len(strin),pick)
    for i in range(0,len(list1)):
        temp=temp+list1[i]
    encrypted_msg=ran3()+temp+ran3()
    return encrypted_msg

def decrypt(strin):
    list2=[]
    temp2=''
    decrypted_msg=''
    if len(strin)<=3:
        for i in range (0,len(strin)):
           temp2=strin[i]+temp2
        return temp2
    for i in range(3,len(strin)-3):
        list2.append(strin[i])
    temp2=list2.pop(-1)
    list2.insert(0,temp2)
    for i in range(0,len(list2)):
        decrypted_msg=decrypted_msg+list2[i]
    return decrypted_msg

def type():
    word=input('Enter your Sentence :')
    ask=input('\nEnter "e" to Encode or "d" to decode :')
    if ask=='e':
        print('\nProcessing', end = '')
        Dot(8)
        print('\n'+EsentenceSpilt(word))
    elif ask=='d':
        print('\nProcessing', end = '')
        Dot(8)
        try:
            print('\n'+DsentenceSpilt(word))
        except:
            print('\nI think you are trying to Decrypt a Decrypted message -_-')
    else:
        print('\nFollow the instructions', end = '')
        Dot()
        print('')
        type()

def main():
    type()
    sleep(1)
    again=input('\nAgain ?(y or n) :')
    print('\n')
    if again=='y':
        main()
    else:
        exit()
main()