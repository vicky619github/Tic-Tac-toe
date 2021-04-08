# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:46:36 2021

@author: vignesh jaishankar
"""

def drawField(field):
    for row in range(5):#0 1 2 3 4 
                        #0 . 1 . 2 
        if row%2 == 0:  #0,2,4
            practicalrow = int(row/2) #0 1 2
            for coloum in range(5):#0 1 2 3 4
                                   #0 . 1 . 2
                if coloum%2 == 0: #0,2,4
                    practicalColoum = int(coloum/2) #0 1 2
                    if coloum != 4:                 
                        print(field[practicalColoum][practicalrow],end ="")
                    else:
                        print(field[practicalColoum][practicalrow])                   
                else:
                    print("|",end = "")
        else:
            print("-----")
player = 1
currentField = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
drawField(currentField)
while(True):
    print("players turn: ",player)
    moveRow = int(input("please enter the row\n"))
    moveColoum = int(input("please enter the column\n"))
    if player == 1:
        if currentField[moveColoum][moveRow] == " ": #empty ya eruka nu pakkum
           currentField[moveColoum][moveRow] = "X"
           player = 2
    else:
        if currentField[moveColoum][moveRow] == " ":
           currentField[moveColoum][moveRow] = "O"
           player = 1
    drawField(currentField)
    