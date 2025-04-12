
###COMPLETED###

import os
import glob

def clear(path, exten):
    os.chdir(path)
    file_list = glob.glob("*." + extention)
    #print(file_list)
    i = 1
    for file in file_list:
        os.rename(file, str(i) + "." + extention)
        i += 1

path = input("Enter the path (Blank for current directory) :")
if path == '':
    path = os.getcwd()
extention = input("What is the extention of the files (txt, png, jpeg etc..) :")

clear(path, extention)

print("Done")
    
