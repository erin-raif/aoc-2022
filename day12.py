# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:27:06 2022

@author: eeenr
"""

import numpy as np
import string

class Coords:
    # Note Y increases DOWNWARDS. X as usual L-R
    def __init__(self, x, y, steps):
        self.x = x
        self.y = y
        self.steps = steps
        return
    def __eq__(self, c):
        return (c.x == self.x and c.y == self.y)
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
def get_height(grid, loc):
    return grid[loc.y][loc.x]


def make_grid(in_grid):
    grid = []
    for g in in_grid:
        new_row = [50]
        for letter in g:
            if letter == 'S':
                new_row.append(0)
            elif letter == 'E':
                new_row.append(27)
            else:
                new_row.append(lower_case.index(letter)+1)
        new_row.append(50)
        grid.append(new_row)
                
    grid.append([50]*len(grid[0]))
    grid.insert(0,[50]*len(grid[0]))
    grid = np.array(grid)
    return grid


def BFS(grid, start_point, end_point, max_steps=None):
    visited = [start_point]
    queue = [start_point]

    while queue:
        current_loc = queue.pop(0)
        if max_steps != None:
            if current_loc.steps > max_steps:
                return current_loc.steps
        if current_loc.x == end_point.x and current_loc.y == end_point.y:
            return current_loc.steps
        dx    = 1
        left  = Coords(current_loc.x-dx, current_loc.y,    current_loc.steps+1)
        right = Coords(current_loc.x+dx, current_loc.y,    current_loc.steps+1)
        up    = Coords(current_loc.x,    current_loc.y-dx, current_loc.steps+1)
        down  = Coords(current_loc.x,    current_loc.y+dx, current_loc.steps+1)
        
        neighbours = [left, right, up, down]
        for neighbour in neighbours:
            if (neighbour not in visited
                and get_height(grid, neighbour)
                    <= get_height(grid, current_loc) + 1):
                visited.append(neighbour)
                queue.append(neighbour)
    #print(visited)
    return 1000



lower_case = string.ascii_lowercase

in_grid = open('day12.txt').read().split()
grid = make_grid(in_grid)
# quickly find start and end point
start_y, start_x = np.where(grid == 0)
start_point = Coords(start_x[0], start_y[0], 0)
end_y, end_x = np.where(grid == 27)
end_point = Coords(end_x[0], end_y[0], None)

print('Part 1 answer:', BFS(grid, start_point, end_point))

new_starts = np.where(grid == 1)
steps = [500]
for i in range(len(new_starts[0])):
    if new_starts[1][i] < 4:
        ns = Coords(new_starts[1][i],new_starts[0][i],0)
        print(ns)
        steps.append(BFS(grid, ns, end_point,min(steps)))
print('Part 2 answer:', min(steps))
    


    