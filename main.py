verticle = '|'
horizontal = '-'
plus = '+'
second_move = False
dict1 = {
    1: '-',
    2: '-',
    3: '-',
    4: '-',
    5: '-',
    6: '-',
    7: '-',
    8: '-',
    9: '-'
}

dict_ref = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'
}


def reference():
    itera_odd = True
    x = 9

    for col in range(1, 6):
        if itera_odd == True:
            print(dict_ref[x-2], verticle,
                  dict_ref[x-1], verticle, dict_ref[x])
            itera_odd = False
            if x > 3:
                x -= 3
            else:
                break
        elif itera_odd == False:
            print(horizontal, plus, horizontal, plus, horizontal)
            itera_odd = True


reference()
print('\n\n')

move = False
occupied = 0



def game(second_move,occupied):

    if occupied<9:

        if second_move == False:
            curr_move = 'X'
            try:
                rec_move = int(input('\nFirst Player to move.\n'))
                if rec_move in list(range(1,10)) and dict1[rec_move] == '-':
                    dict1[rec_move] = curr_move
                    occupied+=1
                    second_move = True

                else:
                    print('\nWrong move.\n')
                    game(second_move,occupied)

            except ValueError:
                print('\nInvalid move.\n')

            if dict1[1] == dict1[4] == dict1[7]!='-' or dict1[1] == dict1[5] == dict1[9]!='-' or dict1[1] == dict1[2] == dict1[3]!='-' or dict1[4] == dict1[5] == dict1[6]!='-' or dict1[7] == dict1[8] == dict1[9]!='-' or dict1[3] == dict1[5] == dict1[7]!='-':
                print('\nGame Over.\n')
                print('\n*****X has won*****\n')
                show_game()
                

            elif dict1[2] == dict1[5] == dict1[8]!='-' :
                print('\nGame Over.\n')
                print('\n*****X has won*****\n')
                show_game()

            elif dict1[3] == dict1[6] == dict1[9]!='-':
                print('\nGame Over.\n')
                print('\n*****X has won*****\n')
                show_game()
            
            else:
                show_game()
                game(second_move,occupied)

        else:
            curr_move = 'O'
            try:
                rec_move = int(input('\nSecond Player to move.\n'))
                if rec_move in list(range(1, 10)) and dict1[rec_move] == '-':
                    dict1[rec_move] = curr_move
                    occupied+=1
                    second_move = False
                else:
                    print('\nWrong Move.\n')
                    game(second_move,occupied)

            except ValueError:
                print('\nInvalid move.\n')

            if dict1[1] == dict1[4] == dict1[7] != '-' or dict1[2] == dict1[5] == dict1[8] != '-' or dict1[3] == dict1[6] == dict1[9] != '-' or dict1[1] == dict1[5] == dict1[9] != '-' or dict1[1] == dict1[2] == dict1[3] != '-' or dict1[4] == dict1[5] == dict1[6] != '-' or dict1[7] == dict1[8] == dict1[9] != '-' or dict1[3] == dict1[5] == dict1[7] != '-':
                show_game()
                print('\nGame Over.\n')
                print('\n*****O has won*****\n')
                

            else:
                show_game()
                game(second_move,occupied)

    else:
        print("\nIt's a Draw\n")
        now_what = input('Wanna play again?(Y/N) ')
        if now_what.upper() =='Y':
            for i in range(1,10):
                dict1[i]='-'
            game(second_move=False,occupied=0)
        elif now_what.upper() == 'N':
            print('\nGame Over.\n')

def show_game():
    itera_odd = True
    x = 9
    for col in range(1, 6):
        if itera_odd == True:
            print(dict1[x-2], verticle, dict1[x-1], verticle, dict1[x])
            itera_odd = False
            if x > 3:
                x -= 3
            else:
                break
        elif itera_odd == False:
            print(horizontal, plus, horizontal, plus, horizontal)
            itera_odd = True


game(second_move,occupied)
