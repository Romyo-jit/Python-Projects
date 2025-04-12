
#Completed

def opening():
    print ('                       Who Will Be Next Millionaire\n\n')
    rules = '1. Player has to write the correct answer to the question displayed in the screen.\n\n2. There will be 10 questions. With every correct answer the money will increase.\n\n3. If you answer incorrect a single time, you can\'t answer upcoming questions. But you will get your previous total money.\n\n4. Only answer in one or two words.\n'
    print(rules)
    st = input ('Press Enter to start. :')
    pass



def calc():
    Q=[ '\nQ1. What is the capital of Germany ?\n\n:>','Q2. Who is the president of Canada ?\n\n:>', 'Q3. What is the closest star from Sun ?\n\n:>','Q4. What is the last name of the developer who invented Python programming language ?\n\n:>','Q5. Which city is reffer to \'City Of Joy\'  ?\n\n:>','Q6. What is the oldest civilization ?\n\n:>','Q7. What is the toughest object in the earth ?\n\n:>','Q8. What is the saltiest river in the world ?\n\n:>','Q9. Who killed King Kaska ?\n\n:>','Congrats You have made this far. This is the last question.\nQ10. What is the derivative of X with respect to X ?\n\n:> ']
    A=['Berlin', 'Justin Trudo','Proxima Centauri','Python','Kolkata','Maya','Diamond','Jordan','Julias Caeser','1']
    money=['10000','20000','30000','40000','50000','60000','70000','80000','90000','550000']
    i=0
    Total=0
    for i in range(0,10):
     #   ri=randrange(0,5)
        c=input(Q[i])
        if c ==A[i]:
            print('\nCorrect answer you Won '+money[i]+'$\n')
            Total=Total+int(money[i])
            continue
        else:
            print ('No, the answer is '+A[i]+'\n')
            break
    return Total
    pass



def main():
    opening()
    Total=calc()
    if Total != 1000000:
        print ('You have won '+str(Total)+'$\n')
    else:
        print ('Woohooh... You have answered all questions. \nYou have become a milloniare.\n' )
        print('You have won '+str(Total)+'$\n\n')
    last=input('Do you want to play again ?(\'y\' or \'n\')')
    if last =='y':
        print('\n')
        main()
    else:
        exit()
    pass
main()
#print(rn.randrange(0,4))
    