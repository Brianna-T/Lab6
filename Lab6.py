"""
Course CS2302 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 4/2/2019
6th Lab
This lab is over creating our own maze, along with our own path using disjoint set forests.
"""
# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
"""
import random
"""
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    #method for drawing the maze/displaying numbers
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols): #i think creates the set..?
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w
"""
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
"""     
def find(walls,r): #change i value
    # Returns root of tree that i belongs to
    if walls[r]<0:
        return r
    return find(walls,walls[r])

def union(walls,r,c):
    # Joins i's tree and j's tree, if they are different
    #When you remove a wall, if the cells that were separated by that wall
    #belonged to different sets, you must unite these sets.
    ri = find(walls,r) 
    rj = find(walls,c) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        walls[rj] = ri  # Make j's root point to i's root   
       

def unionC(walls,r,c):#union w/ compression
    if walls[r]<0:
        rr=find(walls,r)
        rc=find(walls,c)
        root=walls[r]
        if walls[rc]==rr:
            walls[rc]=root #look over this, prolly not right
            #trying to make if root is similar to other's root, then
            #make it point to original root instead, to reflect what we
            #did in class    

plt.close("all")

#test1 
maze_rows = 10
maze_cols = 15

"""
#test2
maze_rows = 5
maze_cols = 10
"""
"""
#test3
maze_rows = 0
maze_cols = 2
"""
"""
#test4
maze_rows = 1
maze_cols = 5
"""
walls = wall_list(maze_rows,maze_cols)
"""
union(walls,2,4)
union(walls,7,9)
"""

draw_maze(walls,maze_rows,maze_cols,cell_nums=True) #prints figure of numbered maze

"""
#randomly removing walls
for i in range(len(walls)//2): #Remove 1/2 of the walls 
    d = random.randint(0,len(walls)-1)
    print('removing wall ',walls[d])
    walls.pop(d)
"""
draw_maze(walls,maze_rows,maze_cols) #prints maze w/out numbers