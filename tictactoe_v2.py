"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Michael Čermák
email: michael.cermak92@gmail.com
discord: MichaelCe#8181
"""

import os

### Functions
def welcome():
    fill_introduction = "TICTACTOE"
    print("Welcome to the")
    layout = tab_gen(fill_introduction)
    print("".join(layout))
    pass

def game_introduction():
    fill_guide = "123456789"
    layout = tab_gen(fill_guide)
    print("""
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row

Grid is filled with numbers as follows:
""")
    print("".join(layout))
    pass

def tab_gen(fill):
    #variable for end of the line
    rowend = 0
    #indicies of fillable "cells" with X/O
    index = 0
    #list for layout of generated tab
    layout = []
    tab = ["+", "-", "|", " ", "\n"]
    for n in range(49):
        
        #corners
        if n == 0:
            layout.append(tab[0])
        elif n % 14 < 8 and n % 2 == 0 and n > 0:
            layout.append(tab[0])

            #end of line
            if  (n - rowend) % 14 == 0 or (n - rowend) - 6 == 0:
                layout.append(tab[4])
                rowend = n
        
        #dash
        if n % 14 < 8 and n % 2 != 0 and n > 0 and (n - rowend != 1 or n == 1):
            layout.append(tab[1].center(3))
              
        #pipe
        if (n - rowend) % 14 < 8 and n % 2 == 1 and rowend > 0: # 
                layout.append(tab[2])           
                if n - rowend == 7:
                    layout.append(tab[4])
        
        #game "cells"
        if (n - rowend) % 14 < 8 and n > rowend and n % 2 == 0 and rowend > 0:
                layout.append(fill[index].center(3))
                index = index + 1           
    return layout

def user_input():   
    while True:
        try:
            index_xo = int(input("Enter the position number from range 1-9:"))
            #print(index_xo)
            #print(fill)
            if index_xo < 1 or index_xo > 9:
                print("Wrong entry!!! Try again")
                continue
            if fill[index_xo - 1] == "X" or fill[index_xo - 1] == "O":
                print("You cannot overwrite previous turns! \n" 
                  "Try again! Your entry was " + str(index_xo))
                continue
            return index_xo       
        except ValueError:
            print("Wrong entry!!! Try again")
            continue
        
def fill_xo(user_choice): 
    global player
    if player == 1:
        fill[user_choice-1] = "X"
        player = 2
    else:
        fill[user_choice-1] = "O"
        player = 1
    pass

###

os.system("cls")
game_end = False
fill = list("123456789")
player = 1
welcome()
game_introduction()
counter = 0
while game_end is not True:   
    counter += 1
    if player == 1:
        print("Player X")
    else:
        print("Player O")

    user_input_index = user_input()
    fill_xo(user_input_index)
    layout = tab_gen(fill)
    print("".join(layout))

    if (
         fill[0] == fill[1] == fill[2] != " " or
         fill[3] == fill[4] == fill[5] != " " or
         fill[6] == fill[7] == fill[8] != " " or
         fill[0] == fill[3] == fill[6] != " " or
         fill[1] == fill[4] == fill[7] != " " or
         fill[2] == fill[5] == fill[8] != " " or
         fill[0] == fill[4] == fill[8] != " " or
         fill[2] == fill[4] == fill[6] != " "
        ):
          #winner announcement
        if player == 2:
            print()
            print("Player X wins, CONGRATULATIONS!!!")

        elif player == 1:
            print()
            print("Player O wins CONGRATULATIONS!!!")
        game_end = True
    
    elif counter == 9:
        print("It is a TIE! Noone wins :(\n")     
        game_end = True