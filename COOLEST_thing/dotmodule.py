from time import sleep

def Dot(dots = 5): #Defalt value 5 dots
    i = 0
    while i != dots:
        sleep(.2)
        print('.', end = '', flush = True)
        i += 1

if __name__ == "__main__":
    print("This is a module, not a program. Ok I will show you what it does.")
    sleep(1)
    print("It prints a dot every 0.2 seconds. Like this:", end='')
    Dot(20)
    sleep(1)
    print("\nlol")