import random as rn
def t_d():
    pla=input('Enter "2" for Two players or "4" for Four players-- ')
    if pla=='2':
        guess=rn.randint(0,1)
        noth=input('\nPlayer 1 sit here. -->\n\n<-- Here Player 2.\n\nEnter anything to Start.')
        print('\nChoosing......\n')
        if guess==0:
            print('-->')
        else:
            print('<--')
        print('\n')
    elif pla=='4':
        guess=rn.randint(0,3)
        noth=input('\nPlayer 1 sit here. -->\n\n<-- Here Player 2.\n\n^ Here Player 3.\n\nv Player 4 here.\n\nEnter anything to Start.')
        print('\nChoosing......\n')
        if guess==0:
            print('-->')
        elif guess==1:
            print('<--')
        elif guess==2:
            print('^')
        else:
            print('v')
        print('\n')
    else:
        print('Wrong input. Start over...\n')
        t_d()
    t_d()
t_d()