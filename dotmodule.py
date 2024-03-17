from time import sleep

def Dot(dots = 5): #Defalt value 5 dots
    i = 0
    while i != dots:
        sleep(.2)
        print('.', end = '', flush = True)
        i += 1