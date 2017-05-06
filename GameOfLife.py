# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:33:20 2017

@author: Joseph Perkins
"""
from tkinter import *
def main():
    global GRID_WIDTH, GRID_HEIGHT
    GRID_WIDTH = 20
    GRID_HEIGHT = 20
    root = Tk()
    frame=Frame(root)
    frame.grid(row=0,column=0)

    btn=  [[0 for x in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]
    createWidgets(root,frame, btn)

    #nxt=  [[0 for x in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)]
    #createWidgets(root,frame, nxt) # no display

    root.mainloop()


def createWidgets(root,frame, btn):
    for x in range(GRID_WIDTH):
         for y in range(GRID_HEIGHT):
            btn[x][y] = [Button(frame,command= lambda x1=x, y1=y: color_change(btn,x1,y1),width = 2), "dead"]
            btn[x][y][0].grid(column=x, row=y)

    play = Button(frame, command = lambda: playGame(btn), text = "Play", width = 6, height = 2)
    play.grid(row = 40, column = x+5)


def color_change(btn, x,y):
    if btn[x][y][1] == "dead":
        btn[x][y][0].config(bg="black")
        btn[x][y][1] = "alive"
    else:
        btn[x][y][0].config(bg="white")
        btn[x][y][1] = "dead"


def playOrStop():
    pass
    #later make a button to play and stop during the simulation


def playGame(btn):
    """
    nextMove = btn
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            adjacent = 0
            for i in range(x-1, x+2):
                for j in range(y-1,y+2):

                    if i < GRID_WIDTH and i >= 0 and j >=0 and j < GRID_HEIGHT:
                        if btn[i][j][1] == "alive" and btn[i][j] != btn[x][y]:
                            adjacent += 1
            if adjacent == 1:
                nextMove[x][y][1] ="alive"
                print("durp")
            else:
                nextMove[x][y][1] = "dead"

    btn = nextMove
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if btn[x][y][1] == "alive":
                btn[x][y][0].config(bg="black")
            else:
                btn[x][y][0].config(bg="white")
                """
    test_game_state_step()


# Game state as [[Bool]]

def game_state_step(game_state):
    '''Returns a new game state as double list, [[Bool]].'''
    nxt = [[False for j in range(len(game_state))] for j in range(len(game_state[0]))]
    for x in range(len(game_state)):
        for y in range(len(game_state[0])):
            adjacent = 0
            for i in range(x-1, x+2):
                for j in range(y-1,y+2):
                    if i < len(game_state) and i >= 0 and j >=0 and j < len(game_state[0]):
                        if game_state[i][j] == True and not (x==i and y== j):
                            adjacent +=1
            print(x,y, adjacent)
                            
            if game_state[x][y] == True:
                if adjacent == 3 or adjacent == 2:
                    nxt[x][y] = True
                else:
                    nxt[x][y] = False
            else:
                if adjacent == 3:
                    nxt[x][y] = True
                else:
                    nxt[x][y] = False
                               
    return nxt # TODO


def test_game_state_step():
    '''Tests the game_state_step function!'''
    state1 = (
        [[False, False, False, False, False, False],
         [False, False, False, True,  False, False],
         [False, True,  False, True,  False, False],
         [False, False, True,  True,  False, False],
         [False, False, False, False, False, False],
         [False, False, False, False, False, False]])
    expected_state2 = (
        [[False, False, False, False, False, False],
         [False, False, True,  False, False, False],
         [False, False, False, True,  True,  False],
         [False, False, True,  True,  False, False],
         [False, False, False, False, False, False],
         [False, False, False, False, False, False]])
    state2 = game_state_step(state1)
    # Check lengths
    height = len(state1)
    width = len(state1[0])
    next_height = len(state2)
    next_width = len(state2[0])
    if height != next_height or width != next_height:
        print("TEST FAILED! Length mismatch!")
        return
    for y in range(height):
        for x in range(width):
            if expected_state2[y][x] != state2[y][x]:
                print("TEST FAILED! Bad cell value @ ({}, {})!".format(x, y))
                print(state2)
                return


main()
