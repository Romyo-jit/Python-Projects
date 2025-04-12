#COMPLETED

from random import randrange

opts = ['Snake', 'Water', 'Gun']
wins = ['Gun', 'Snake', 'Water']

def main():
    p_choose = opening()
    c_choose = opts[randrange(0,3)]
    #print(f"{p_choose = }", f"{c_choose = }")
    game(p_choose, c_choose)
    
def opening():
    try:
        p_choose = int(input('Choose butween Snake, Water, Gun as 1, 2 or 3 :'))
        print('\n')
    except:
        print('Enter valid choice..')
        main()
    if p_choose > 3 or p_choose < 1:
        print('Enter valid choice..')
        main()
    else:
        return opts[p_choose - 1]

def game(player, computer):
    if player == computer :
        print(f'You and Computer both chose {player}. So the game is Draw.')
    elif player == opts[0] and computer == wins[0]:
        print(f"You chose {player} and Computer chose {computer}. So Computer Won.")
    elif player == opts[1] and computer == wins[1]:
        print(f"You chose {player} and Computer chose {computer}. So Computer Won.")
    elif player == opts[2] and computer == wins[2]:
        print(f"You chose {player} and Computer chose {computer}. So Computer Won.")
    else: 
        print(f"You chose {player} and Computer chose {computer}. So You Won.")
    temp = int(input('\nDo You want to play again ?(1 or 0) :'))
    if temp == 1:
        print('\n')
        main()
        
       
main()