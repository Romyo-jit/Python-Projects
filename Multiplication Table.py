def main():
    inp = input('Write the number whose multiplication table you want :')
    inp=int(inp)
    for i in range(1,11):
        print(str(inp)+' x '+str(i)+' = '+str(i*inp))
    cont=input('Do you want to continue ?(\'y\' or\'n\') :')
    if cont=='y':
        main()
    else:
        exit()
main()