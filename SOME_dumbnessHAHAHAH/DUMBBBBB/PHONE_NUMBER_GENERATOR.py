import random as rn
def generate():
    a=input('Type anything to generate-- ')
    pNum=rn.randrange(8000000000,9999999999)
    print(pNum)
    generate()
generate()