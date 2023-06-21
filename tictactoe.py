"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michael Čermák
email: michael.cermak92@gmail.com
discord: MichaelCe#8181
"""

import os

tab = ["+", "-", "|", " "]
t = "TICTACTOE"
ttt = list(t)
separator = 41 * "="

#function for game grid generating
def tab_gen():
    #variable for end of the line
    rowend = 0
    #indicies of fillable "cells" with X/O
    index = 0
    #list for layout of generated tab
    layout = []

    for n in range(49):
        
        #corners
        if n == 0:
            print(tab[0], end="")
            layout.append(tab[0])
        elif n % 14 < 8 and n % 2 == 0 and n > 0:
            print(tab[0], end="")
            layout.append(tab[0])

            #end of line
            if  (n - rowend) % 14 == 0 or (n - rowend) - 6 == 0:
                print()
                rowend = n
        
        #dash
        if n % 14 < 8 and n % 2 != 0 and n > 0 and (n - rowend != 1 or n == 1):
            print(tab[1].center(3), end="")
            layout.append(tab[1].center(3))
        
        
        #pipe
        if (n - rowend) % 14 < 8 and n % 2 == 1 and rowend > 0: # 
                print(tab[2], end="")
                layout.append(tab[2])           
                if n - rowend == 7:
                    print()
        
        #game "cells"
        if (n - rowend) % 14 < 8 and n > rowend and n % 2 == 0 and rowend > 0:
                print(ttt[index].center(3), end="")
                layout.append(tab[3].center(3))
                index = index + 1           
    print() #making space after the example is printed

os.system('cls')

#game introduction
print(separator)
print("Welcome to the")
tab_gen()

#rules
txt= """
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row

Grid is filled with numbers as follows:
"""
ttt = list()

#grid fill with number positions
for n in range(1,10):
    ttt.append(str(n))

print(txt)
tab_gen()
ttt = list(" " * 9)
player = 1
win = False

#game
while win is not True:

#user input
    if player == 1:
        print("Player X")
    else:
        print("Player O")
    
    while True:
        try:
            xo = int(input("Enter the position number from range 1-9:"))
        except ValueError:
            print("Wrong entry!!! Try again")
            continue
        if xo < 1 or xo > 9:
            print("Wrong entry!!! Try again")
            continue
        xo = xo - 1

        #user tries to overwrite
        if ttt[int(xo)] != " ":
            print("You cannot overwrite previous turns! \n" 
                  "Try again! Your entry was " + str(xo+1))
            continue
        else:
            if player == 1:
                ttt[int(xo)] = "X"
                player = 2
            else:
                ttt[int(xo)] = "O"
                player = 1
            break

    #win condition
    if (
         ttt[0] == ttt[1] == ttt[2] != " " or
         ttt[3] == ttt[4] == ttt[5] != " " or
         ttt[6] == ttt[7] == ttt[8] != " " or
         ttt[0] == ttt[3] == ttt[6] != " " or
         ttt[1] == ttt[4] == ttt[7] != " " or
         ttt[2] == ttt[5] == ttt[8] != " " or
         ttt[0] == ttt[4] == ttt[8] != " " or
         ttt[2] == ttt[4] == ttt[6] != " "
        ):
          #winner announcement
          if player == 2:
            print()
            print("Player X wins, CONGRATULATIONS!!!")
          else:
            print()
            print("Player O wins CONGRATULATIONS!!!")

          win = True
    
    tab_gen()