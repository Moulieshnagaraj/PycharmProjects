# project on hangman
'''
0123456789.,.,
 ___________     0
|/         |     1
|         ---    2
|        |   |   3
|         ---    4
|          |     5
|         /|\    6
|        / | \   7
|          |     8
|          |     9
|         / \    10
|        /   \   11
 -----------     12
'''
from termcolor import colored, cprint
import random


# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

print('\n')
cprint("***** H-A-N-G-M-A-N *****",'red','on_cyan',attrs=['reverse','blink'])
cprint('1.Player 1','red')
cprint('2.Player 2','red')


word=[]

f=open('cricket.txt','r')
for i in f.readlines():
    word.append(i.strip())
f.close()






def base():
    for col in range(14):
        if col == 0:
            for row in range(13):
                cprint('|','blue')
        if col>0:
            for row in range(1):
                cprint('=','blue',end='')



def top():


    for col in range(14):
        if col > 0 and col < 12:
            for row in range(13):
                if row==0:
                    cprint('_','blue',end='')
                    if col==11:
                        cprint('_','blue')
    for col in range(14):
        if col == 0:
            for row in range(13):
                if row > 0:
                    if row==1:
                        cprint('|/','blue')
                    cprint('|','blue')
        if col>0:
            for row in range(1):
                cprint('=','blue',end='')

def head():
    cprint("                ______________", 'blue')
    cprint('                |/         |', 'blue')
    cprint('                |         ---', 'blue')
    cprint("                |        /   \ ", 'blue')
    cprint('                |       | 0 0 |', 'blue')
    cprint('                |         ---', 'blue')
    cprint('                |             ', "blue")
    cprint("                |             ", "blue")
    cprint("                |             ", "blue")
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                ==============", 'blue')




def body():
    cprint("                ______________", 'blue')
    cprint('                |/         |', 'blue')
    cprint('                |         ---', 'blue')
    cprint("                |        /   \ ", 'blue')
    cprint('                |       | 0 0 |', 'blue')
    cprint('                |         ---', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |          |', 'blue')
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                |     ", 'blue')
    cprint("                ==============", 'blue')


def hands():
    cprint('                ______________','blue')
    cprint('                |/         |', 'blue')
    cprint('                |         ---', 'blue')
    cprint("                |        /   \ ", 'blue')
    cprint('                |       | 0 0 |', 'blue')
    cprint('                |         ---', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |         /|\ ', 'blue')
    cprint('                |       \/ | \/ ', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |          |', 'blue')
    cprint('                |','blue')
    cprint('                |', 'blue')
    cprint('                |', 'blue')
    cprint('                ===============','blue')




def legs():
    cprint('                ______________', 'blue')
    cprint('                |/         |', 'green')
    cprint('                |         ---', 'green')
    cprint("                |        /   \ ", 'green')
    cprint('                |       | 0 0 |', 'green')
    cprint('                |         ---', 'green')
    cprint('                |          |', 'green')
    cprint('                |         /|\ ', 'green')
    cprint('                |       \/ | \/ ', 'green')
    cprint('                |          |', 'green')
    cprint('                |          |', 'green')
    cprint('                |         / \ ', 'green')
    cprint('                |        /   \ ', 'green')
    cprint('                |', 'blue')
    cprint('                |', 'blue')
    cprint('                |', 'blue')
    cprint('                ===============', 'blue')


def player1():


    print('HINT: cricket players names')
    turns=5
    random_word=random.choice(word)
    guessmade = ""

    used = []

    while turns>=0:

        if turns == 5:
            base()

        if turns==4:
            top()

        if turns==3:
            head()

        if turns==2:
            body()

        if turns==1:
            hands()

        if turns==0:
            legs()

            cprint("You let a good man to die!!",'red',"on_yellow",attrs=["bold"])
            break




        print('\n')
        count=0

        for char in random_word:
            if char in guessmade:
                print(char,end='')
                count+=1
                if count==len(random_word):
                    print('\n')
                    cprint("Hurrah!!!...YOU SAVED A GOOD MAN",'blue',attrs=['bold'])

                    return False

            else:
                print("_ ",end='')

        print('\n')
        ask=input("enter the character..:").lower().strip()
        used.append(ask)
        print('letters used:',used)
        if ask.isalpha():
            if ask in random_word:
                guessmade=guessmade+ask
            else:
                turns-=1
                cprint("Oops!. wrong guess.",'red')
                print("only {} turns left".format(turns))
        else:
            cprint("Invalid character..",'red','on_magenta')


def player2():
    print('HINT: cricket players names')
    turns = 5
    num=1
    for w in word:
        print(num,'.',w)
        num+=1

    choose=input("Enter the word from the list above").lower().strip()


    random_word=choose

    guessmade = ""

    used = []

    while turns >= 0:

        if turns == 5:
            base()

        if turns == 4:
            top()

        if turns == 3:
            head()

        if turns == 2:
            body()

        if turns == 1:
            hands()

        if turns == 0:
            legs()

            cprint("You let a good man to die!!", 'red', "on_yellow", attrs=["bold"])
            break

        print('\n')
        count = 0

        for char in random_word:
            if char in guessmade:
                print(char, end='')
                count += 1
                if count == len(random_word):
                    print('\n')
                    cprint("Hurrah!!!...YOU SAVED A GOOD MAN", 'blue', attrs=['bold'])

                    return False

            else:
                print("_ ", end='')

        print('\n')
        print('letters used:', used)
        ask = input("enter the character..:").lower().strip()
        used.append(ask)

        if ask.isalpha():
            if ask in random_word:
                guessmade = guessmade + ask
            else:
                turns -= 1
                cprint("Oops!. wrong guess.", 'red')
                print("only {} turns left".format(turns))
        else:
            cprint("Invalid character..", 'red', 'on_magenta')


mode=input("Choose the mode:").strip()
if mode=='1' or mode=='player1' or mode=='PLAYER1':

    player1()
if mode=='2' or mode=='player2' or mode=='PLAYER2':
    player2()


