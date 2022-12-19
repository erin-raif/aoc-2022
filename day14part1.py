# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:54:45 2022

@author: eeenr
"""
import numpy as np

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
def draw_line(grid, c1, c2):
    if c1.x == c2.x and c2.y > c1.y:
        for y in range(abs(c2.y-c1.y)+1):
            grid[c1.y + y][c1.x] = '#'
    elif c1.x == c2.x and c2.y < c1.y:
        for y in range(abs(c2.y-c1.y)+1):
            grid[c1.y - y][c1.x] = '#'
    elif c1.y == c2.y and c2.x > c1.x:
        for x in range(abs(c2.x-c1.x)+1):
            grid[c1.y][c1.x + x] = '#'
    elif c1.y == c2.y and c2.x < c1.x:
        for x in range(abs(c2.x-c1.x)+1):
            grid[c1.y][c1.x - x] = '#'
    return grid

def drop_sand(grid):
    current_x = 500
    current_y = 0
    end = False
    at_rest = False
    abyss = False
    while not end:
        if current_y + 1 == len(grid):
            end = True
            abyss = True
        else:
            if grid[current_y+1][current_x] == '.':
                current_y += 1
            elif grid[current_y+1][current_x-1] == '.':
                current_y += 1
                current_x -= 1
            elif grid[current_y+1][current_x+1] == '.':
                current_y += 1
                current_x += 1
            else:
                end = True
                at_rest = True
    grid[current_y][current_x] = 'o'
    return grid, at_rest, abyss

lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')
lines = open('day14.txt').read().split('\n')

grid = [['.'] * 1000]*170
grid = np.array(grid, dtype=str)

for line in lines:
    coords = line.split(' -> ')
    cs = []
    for c in coords:
        x, y = c.split(',')
        cs.append(Coords(int(x),int(y)))
    for i in range(len(cs)-1):
        grid = draw_line(grid,cs[i],cs[i+1])

grid[0][500] = '+'
#print(grid)
count = 0
abyss = False
while not abyss:
    grid, at_rest, abyss = drop_sand(grid)
    if at_rest:
        count += 1
#print(grid)
print(count)
