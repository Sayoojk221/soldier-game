
board = [
    ['-','-','G','-','-','-','-'],
    ['P','P','P','P','P','P','P'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','B','-','R','R','-','B'],
]

def trap_generator():
    import random
    trap = []
    for i in range(3):
        row = random.randint(2,5)
        column = random.randint(2,5)
        trap.append([row,column])
    return trap

score = 0

print('')
print('Game starts now >>')

def game_display(win=None):
    game_trap = trap_generator()
    print('')
    top = f'   0 1 2 3 4 5 6  '
    print(top)
    print(' + = = = = = = = + ')
    for i in range(7):
        print(str(i)+'|',end=' ')
        for j in range(7):
            print(board[i][j],end=" ")
        print('|'+str(i),end=' ')
        print('')
    print(' + = = = = = = = + ')
    buttom = f'   0 1 2 3 4 5 6   '
    print(buttom)
    print('')
    print('Your score: '+str(score))
    print('')
    if win == None:
        print('This board has '+str(len(game_trap))+' hidden traps!')
    elif win:
        print('You Win! Final score: '+str(score))
    elif not win:
        print('Game over!')




def Gmove():
    import random
    column = random.randint(0,6)
    for i in range(7):
        if board[0][i] in ['-','G']:
            board[0][i] = '-'

    if board[0][column] in ['R','B']:
        board[0][column+2] = 'G'
    else:
        board[0][column] = 'G'


def check_trap(current_pos,new_pos):
    game_trap = trap_generator()
    buttom = [['6','0'],['6','1'],['6','2'],['6','3'],['6','4'],['6','5'],['6','6']]
    start_row = int(current_pos[0])
    futur_row = int(new_pos[0])
    start_colomn = int(current_pos[1])
    future_colomn = int(new_pos[1])

    if current_pos in buttom and new_pos in buttom:
        return False
    elif futur_row == 0 and start_row in [2,3,4,5,6]:
        return False
    elif futur_row == 0 and start_row == 0:
        return False
    elif ((futur_row == 1) and (start_row in [2,3,4,5,6])) and (board[start_row][start_colomn] == 'R'):
        while start_row > 1:
            if start_row == 2:
                if start_colomn >= future_colomn:
                    while start_colomn >= future_colomn:
                        if [start_row,start_colomn] in game_trap:
                            return [start_row,start_colomn]
                        else:
                            if [start_row,start_colomn] == [2,future_colomn]:
                                return False
                            else:
                                if start_colomn > 0:
                                    start_colomn -= 1
                                else:
                                    return False
                elif start_colomn <= future_colomn:
                    while start_colomn <= future_colomn:
                        if [start_row,start_colomn] in game_trap:
                            return [start_row,start_colomn]
                        else:
                            if [start_row,start_colomn] == [2,future_colomn]:
                                return False
                            else:
                                if start_colomn < 7:
                                    start_colomn += 1
                                else:
                                    return False
            else:
                if [start_row,start_colomn] in game_trap:
                    return [start_row,start_colomn]
                else:
                    start_row -= 1

    else:
        if (start_row >= futur_row) and (board[start_row][start_colomn] == 'R'):
            while start_row > 1:
                if start_row == futur_row:
                    if start_colomn <= future_colomn:
                        while start_colomn <= future_colomn:
                            if [start_row,start_colomn] in game_trap:
                                return [start_row,start_colomn]
                            else:
                                if [start_row,start_colomn] == [futur_row,future_colomn]:
                                    return False
                                else:
                                    if start_colomn <= 6:
                                        start_colomn += 1
                                    else:
                                        return False

                    elif start_colomn >= future_colomn:

                        while start_colomn >= future_colomn:
                            if [start_row,start_colomn] in game_trap:
                                return [start_row,start_colomn]
                            else:
                                if [start_row,start_colomn] == [futur_row,future_colomn]:
                                    return False
                                else:
                                    if start_colomn >= 1:
                                        start_colomn -= 1
                                    else:
                                        return False
                else:
                    if [start_row,start_colomn] in game_trap:
                        return [start_row,start_colomn]
                    else:
                        if [start_row,start_colomn] == [futur_row,future_colomn]:
                            return False
                        else:
                            if start_row >= 2:
                                start_row -= 1
                            else:
                                return False
        elif (start_row < futur_row) and (board[start_row][start_colomn] == 'R'):
            while start_row <= 5:
                if futur_row == start_row:
                    if start_colomn <= future_colomn:
                        while start_colomn <= future_colomn:
                            if [start_row,start_colomn] in game_trap:
                                return [start_row,start_colomn]
                            else:
                                if [start_row,start_colomn] == [futur_row,future_colomn]:
                                    return False
                                else:
                                    if start_colomn <= 6:
                                        start_colomn += 1
                                    else:
                                        return False
                    elif start_colomn >= future_colomn:
                        while start_colomn >= future_colomn:
                            if [start_row,start_colomn] in game_trap:
                                return [start_row,start_colomn]
                            else:
                                if [start_row,start_colomn] == [futur_row,future_colomn]:
                                    return False
                                else:
                                    if start_colomn >= 1:
                                        start_colomn -= 1
                                    else:
                                        return False
                else:
                    if [start_row,start_colomn] in game_trap:
                        return [start_row,start_colomn]
                    else:
                        if start_row <= 5:
                            start_row += 1
                        else:
                            return False
        elif (start_row > futur_row) and (board[start_row][start_colomn] == 'B'):
            if (start_row > futur_row ) and (start_colomn < future_colomn):
                while start_row >= futur_row:
                    if [start_row,start_colomn] in game_trap:
                        return [start_row,start_colomn]
                    else:
                        if [start_row,start_colomn] == [futur_row,future_colomn]:
                            return False
                        else:
                            if start_row == futur_row:
                                return False
                            else:
                                start_row -= 1
                                start_colomn += 1

                return False

            else:
                while start_row >= futur_row:
                    if [start_row,start_colomn] in game_trap:
                        return [start_row,start_colomn]
                    else:
                        if [start_row,start_colomn] == [futur_row,future_colomn]:
                            return False
                        else:
                            if start_row == futur_row:
                                return False
                            else:
                                start_row -= 1
                                start_colomn -= 1

                return False
        elif (start_row < futur_row) and (board[start_row][start_colomn] == 'B'):
            if (start_row < futur_row ) and (start_colomn > future_colomn):
                while start_row <= futur_row:
                    if [start_row,start_colomn] in game_trap:
                        return [start_row,start_colomn]
                    else:
                        if [start_row,start_colomn] == [futur_row,future_colomn]:
                            return False
                        else:
                            if start_row == futur_row:
                                return False
                            else:
                                start_row += 1
                                start_colomn -= 1

                return False
            else:
                while start_row <= futur_row:
                    if [start_row,start_colomn] in game_trap:
                        return [start_row,start_colomn]
                    else:
                        if [start_row,start_colomn] == [futur_row,future_colomn]:
                            return False
                        else:
                            if start_row == futur_row:
                                return False
                            else:
                                start_row += 1
                                start_colomn += 1

                return False

def message(trap_value,status):
    global score
    if status == 0:
        print('')
        print('Another soldier is already there. Invalid Move!')
        main()
    elif status == 1:
        score += -2
        print('')
        print('There was a trap at '+str(trap_value)+' Your soldier dies!')
        main()
    elif status == 2:
        score += 1
        main()
    elif status == 3:
        main()
    elif status == 4:
        print('')
        print('The soldier cannot pass a Pawn.')
        main()
    elif status == 5:
        score += 10
        game_display(win=True)
    elif status == 6:
        game_display(win=False)
    elif status == 7:
        print('')
        print('Invalid move for B.')
        main()

def data_insert(trap_value,current_pos,new_pos):
    start_row = int(current_pos[0])
    futur_row = int(new_pos[0])
    start_colomn = int(current_pos[1])
    future_colomn = int(new_pos[1])
    if trap_value:
        if ([trap_value[0],trap_value[1]] != [futur_row,future_colomn]) and (trap_value[0] == futur_row):
            return 7
        else:
            board[trap_value[0]][trap_value[1]] = 'T'
            board[start_row][start_colomn] = '-'
            return 1
    elif futur_row == 1 and not trap_value:
        value_exist = validate(current_pos,new_pos)
        if value_exist:
            return value_exist
        else:
            board[futur_row][future_colomn] = board[start_row][start_colomn]
            board[start_row][start_colomn] = '-'
            return 2

    elif not trap_value:
        validate_entry = validate(current_pos,new_pos)
        if validate_entry == 1:
            return 7
        elif validate_entry == 0:
            return validate_entry
        else:
            if validate_entry == 'crossed':
                if start_row == 0 and futur_row == 0:
                    if board[futur_row][future_colomn] == 'G':
                        board[futur_row][future_colomn] = board[start_row][start_colomn]
                        board[start_row][start_colomn] = '-'
                        return 5
                    else:
                        return 3
                elif futur_row == 0 and start_row in [2,3,4,5,6]:
                        return 4
            elif validate_entry == 'not crossed':
                board[futur_row][future_colomn] = board[start_row][start_colomn]
                board[start_row][start_colomn] = '-'
                return 3

def validate(current_pos,new_pos):
    start_row = int(current_pos[0])
    futur_row = int(new_pos[0])
    start_colomn = int(current_pos[1])
    future_colomn = int(new_pos[1])

    if (start_row > futur_row) and (board[start_row][start_colomn] == 'B'):
        if (start_row > futur_row ) and (start_colomn < future_colomn):
            while start_row >= futur_row:
                if ([start_row,start_colomn] != [futur_row,future_colomn]) and (start_row == futur_row):
                    return 1
                else:
                    if [start_row,start_colomn] == [futur_row,future_colomn]:
                        return 'not crossed'
                    else:
                        start_row -= 1
                        start_colomn += 1

            return 'not crossed'
        else:
            while start_row >= futur_row:
                if ([start_row,start_colomn] != [futur_row,future_colomn]) and start_row == futur_row:
                    return 1
                else:
                    if [start_row,start_colomn] == [futur_row,future_colomn]:
                        return 'not crossed'
                    else:
                        start_row -= 1
                        start_colomn -= 1
            return 'not crossed'

    elif (start_row < futur_row) and (board[start_row][start_colomn] == 'B'):
        if (start_row < futur_row ) and (start_colomn > future_colomn):
            while start_row <= futur_row:
                if ([start_row,start_colomn] != [futur_row,future_colomn]) and start_row == futur_row:
                    return 1
                else:
                    if [start_row,start_colomn] == [futur_row,future_colomn]:
                        return 'not crossed'
                    else:
                        start_row += 1
                        start_colomn -= 1

            return 'not crossed'
        else:
            while start_row <= futur_row:
                if ([start_row,start_colomn] != [futur_row,future_colomn]) and start_row == futur_row:
                    return 1
                else:
                    if [start_row,start_colomn] == [futur_row,future_colomn]:
                        return 'not crossed'
                    else:
                        start_row += 1
                        start_colomn += 1

            return 'not crossed'

    elif (futur_row == start_row) and (board[start_row][start_colomn] == 'B') :
        return 1

    value_exist = board[futur_row][future_colomn]
    if value_exist not in ['-','G']:
        return 0
    else:
        if futur_row == 0 and start_row in [2,3,4,5,6]:
            return 'crossed'
        elif start_row == 0 and futur_row == 0:
            return 'crossed'
        else:
            return 'not crossed'



def main(win=None):
    Gmove()
    soldier_count = len([board[6][i] for i in range(7) if board[6][i] !='-'])
    if soldier_count > 0:
        game_display()
        print('')
        while True:

            current_pos = input("To move your soldier enter its's current position <row,col>: ").split(',')
            check = [i for i in current_pos if i.isdigit() if int(i) <= 6]
            if len(check) > 1:
                if board[int(check[0])][int(check[1])] == 'P':
                    print('')
                    print('Do not select pawn ')
                    print('')
                else:
                    value_exist = True if board[int(check[0])][int(check[1])] != '-' else False
                    if value_exist:
                        while True:
                            new_pos = input("Enter the new position <row,col>: ").split(',')
                            check = [i for i in new_pos if i.isdigit() if int(i) <= 6]
                            if len(check) >1:
                                break
                            print('Invalid input, enter again,')
                        break
                    else:
                        print('Nobody is there at '+check[0]+','+check[1])
                        print('')
                        print('Your score: '+str(score))
                        print('')
            else:
                print('Invalid input, enter again,')
        trap_value = check_trap(current_pos,new_pos)
        data_insert_status = data_insert(trap_value,current_pos,new_pos)
        message(trap_value,data_insert_status)
    else:
        trap_value = None
        data_insert_status = 6
        message(trap_value,data_insert_status)

main()
