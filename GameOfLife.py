# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:33:20 2017

@author: Joseph Perkins
"""
from tkinter import *
def main():
    GRID_WIDTH = 50
    GRID_HEIGHT = 30
    root = Tk()
    frame=Frame(root)
    frame.grid(row=0,column=0)
    
    btn=  [[0 for x in range(GRID_HEIGHT)] for x in range(GRID_WIDTH)] 
    createWidgets(root,frame, btn)
    
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
    nextMove = btn
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            adjacent = 0 
            for i in range(x-1, x+2):
                for j in range(y-1,y+2):
                    
                    if i < 50 and i >= 0 and j >=0 and j < 30:
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
                
main()

