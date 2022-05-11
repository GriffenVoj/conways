import pygame as py
import numpy as np


#see whole array (when needed)
import sys
np.set_printoptions(threshold=sys.maxsize)


#constants
screen=(800,800)
cells=screen[1]//10
white=(255,255,255)
black=(0,0,0)

#grid 


#screen
screen = py.display.set_mode(screen)
py.display.set_caption("Conway's Game of Life")
py.display.flip()


#update color function
def update_color(color_grid):
    ones=np.argwhere(color_grid==1)
    zeros=np.argwhere(color_grid==0)
    for item in ones:
        py.draw.rect(screen, white, py.Rect(item[0]*10, item[1]*10, 10, 10))
    for item in zeros:
        py.draw.rect(screen, black, py.Rect(item[0]*10, item[1]*10, 10, 10))
    py.display.flip()
    return

#find neighors - need ot add one to each input
def neighbors(row_number, column_number, neighbor_grid):
     return [[neighbor_grid[i][j] if  i >= 0 and i < len(neighbor_grid) and j >= 0 and j < len(neighbor_grid[0]) else 0
                for j in range(column_number-1-1, column_number+1)]
                    for i in range(row_number-1-1, row_number+1)]

#game updates   
#alive =1, dead =0
#need 2-3 neighors to survive and exactly 3 alive cells to reproduce

def conway(conway_grid):
    ones=np.argwhere(conway_grid==1)
    zeros=np.argwhere(conway_grid==0)
    sub_grid=np.copy(conway_grid)
    #death - only takes in ones
    print(len(ones))
    for item in ones:
        #sum counts self
        if np.sum(neighbors(item[0]+1,item[1]+1,conway_grid))!=3 and np.sum(neighbors(item[0]+1,item[1]+1,conway_grid))!=4:
            sub_grid[item[0]][item[1]]=0
            print("death")
    #life - needs zeros
    for ele in zeros:
        if np.sum(neighbors(ele[0]+1,ele[1]+1,conway_grid))==3:
            sub_grid[ele[0]][ele[1]]=1
    ones=np.argwhere(sub_grid==1)
    print(len(ones))
    return sub_grid




def main():
    run=True
    start=False
    grid=np.zeros((cells,cells))
    py.init()
    while run:
        for event in py.event.get():
            if event.type==py.QUIT:
                run=False
            if event.type == py.MOUSEBUTTONUP:
                pos = py.mouse.get_pos()
                grid[pos[0]//10][pos[1]//10]=1
                update_color(grid)
            if event.type == py.KEYDOWN:
                if event.key==py.K_SPACE:
                    start = not start
                if event.key==py.K_z:
                    grid=np.zeros((cells,cells))
                    update_color(grid)
                    
        if start:
            grid=conway(grid)
            update_color(grid)
              


        
main()

