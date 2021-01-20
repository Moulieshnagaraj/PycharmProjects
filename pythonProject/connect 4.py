"""
0123456789.,.
 | | | | | | 0
-------------1
 | | | | | | 2
-------------3
 | | | | | | 4
-------------5
 | | | | | | 6
-------------7
 | | | | | | 8
-------------9
 | | | | | | 10

"""
import time
import termcolor
from termcolor import colored, cprint

cprint("LET'S START THE GAME....GET READY!!\nRULES TO BE FOLLOWED", 'blue', attrs=['underline'])
text = ['1.User have to enter only the column number', '2.Only two players are allowed',
        '3.Player wins if same coin is get aligned in row,column or an angle']
for i in text:
    time.sleep(2)
    print(i)
print()
cprint("********** CONNECT 4 BEGINS **********",'green')
time.sleep(1)
fieldboard = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
              [" ", " ", " ", " ", " ", " "]]
x = colored('X', 'green', 'on_magenta')
o = colored('O', 'cyan', 'on_red')


def board(field):
    for row in range(11):
        if row % 2 == 0:  # 0,2,4,6,8,10
            pracrow = int(row / 2)  # 0,1,2,3,4,5,
            for column in range(13):
                if column % 2 == 0:  # 0,2,4,6,8,10,12
                    praccol = int(column / 2)

                    if column != 12:  # 0,1,2,3,4,5,6

                        print(field[praccol][pracrow], end='')
                    else:
                        print(field[praccol][pracrow])
                else:
                    cprint('|', 'blue', end='')
        else:
            cprint('-------------', 'blue')


def player(playerturn):
    board(fieldboard)
    print("PLAYER TURN:", playerturn)
    choice = int(input(termcolor.colored("Please, Enter the column number:", 'green').strip()))
    list_count = [1, 2, 3, 4, 5, 6, 7]
    if choice in list_count:
        specific_column = fieldboard[choice - 1]
        if ' ' in specific_column:
            for i in range(5, -1, -1):
                if specific_column[i] == " ":
                    specific_column[i] = colored(playerturn)
                    break
        else:
            cprint("\n<<The column{} has been occupied>>".format(choice), 'red')
            player(playerturn)
    else:
        cprint("***Enter the valid number***", 'blue', 'on_white', attrs=['bold'])
        player(playerturn)


def isvictorycol():
    state = False
    sizeoffield = len(fieldboard)
    for col in range(sizeoffield):
        sizeofcol = len(fieldboard[col])
        counter = 0
        for i in range(1, sizeofcol):
            if fieldboard[col][i - 1] != ' ' and fieldboard[col][i] != ' ' and fieldboard[col][i - 1] == \
                    fieldboard[col][i]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                state = True
                return state
    return state


def isvictoryrow():
    state = False
    sizeofcol = len(fieldboard)  # 7
    for row in range(0, 6):  # (0,6) > 0,1,2,3,4,5
        counter = 0
        for col in range(1, sizeofcol):  # (1,7)> 1,2,3,4,5,6
            if fieldboard[col - 1][row] != ' ' and fieldboard[col][row] != " " and fieldboard[col - 1][row] == \
                    fieldboard[col][row]:
                counter += 1
            else:
                counter = 0
            if counter == 3:
                state = True
                return state
    return state


def forwarddiagnol(tile):
    state = False
    size = len(fieldboard)
    leng = len(fieldboard[0])
    for c in range(leng - 2):
        for r in range(size - 4):
            if fieldboard[c][r] == tile and fieldboard[c + 1][r + 1] == tile and fieldboard[c + 2][r + 2] == tile and \
                    fieldboard[c + 3][r + 3] == tile:
                state = True
                return True
    return state


def backwarddiagnol(tile):
    state = False
    col = len(fieldboard)
    row = len(fieldboard[0])
    for c in range(row - 2):
        for r in range(3, col - 1):
            if fieldboard[c][r] == tile and fieldboard[c + 1][r - 1] == tile and fieldboard[c + 2][r - 2] == tile and \
                    fieldboard[c + 3][r - 3] == tile:
                state = True
                return True

    return state


while True:
    player(x)
    if isvictorycol()==True or isvictoryrow()==True or forwarddiagnol(x)==True or backwarddiagnol(x)==True:
        board(fieldboard)
        cprint('\nX wins!..congrats!', 'green', 'on_cyan', attrs=['bold'])
        break

    player(o)
    if isvictorycol()==True or isvictoryrow()==True or forwarddiagnol(o)==True or backwarddiagnol(o)==True:
        board(fieldboard)
        cprint('\nO wins!..congrats!', 'blue', 'on_grey', attrs=['bold'])
        break
