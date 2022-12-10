# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 07:14:20 2022

@author: eeenr
"""
import numpy as np

inst = open('day09test.txt').read().split('\n')
inst = open('day09.txt').read().split('\n')

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, c1):
        # if two sets of co-ordinates are the same
        if self.x == c1.x and self.y == c1.y:
            return True
        else:
            return False
    def add_to_x(self, i):
        self.x += i
        return
    def add_to_y(self, i):
        self.y += i
        return
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __hash__(self):
        return hash(str(self))
    
class Knot:
    def __init__(self,iD,start_loc):
        self.iD = iD
        self.locs = [start_loc]
        return
    def __repr__(self):
        return 'Knot ID ' + str(self.iD) + \
            ': current loc: ' + str(self.locs[-1])

def printable_grid(knots):
    #note not generalised, hard coding involved.
    xs = []
    ys = []
    for k in knots:
        xs.append(k.locs[-1].x)
        ys.append(k.locs[-1].y)
    grid = np.empty((5,6),dtype=str).tolist()
    for k in range(len(knots)):
        grid[ys[k]][xs[k]] = grid[ys[k]][xs[k]] + str(k)
    
    grid = np.array(grid[::-1][:])
    print(grid)
    return
        
inst = [x[0]*int(x[2:]) for x in inst]
inst = ''.join(inst)
#print(inst)
knots = []
knot_no = 10
for i in range(knot_no):
    knots.append(Knot(i,Coords(0,0)))
    
#print(knots)

for char in inst:
    #print(char)
    head_x = knots[0].locs[-1].x 
    head_y = knots[0].locs[-1].y
    # Move head
    if char == 'R':
        head_x += 1
    elif char == 'L':
        head_x -= 1
    elif char == 'U':
        head_y += 1
    elif char == 'D':
        head_y -= 1
    knots[0].locs.append(Coords(head_x, head_y))
    for i in range(knot_no-1):
        knot_ahead_x = knots[i].locs[-1].x
        knot_ahead_y = knots[i].locs[-1].y
        this_knot_x = knots[i+1].locs[-1].x
        this_knot_y = knots[i+1].locs[-1].y
        # Move tail - the ugliest if-else control ever
        if abs(knot_ahead_x - this_knot_x) <= 1 and abs(knot_ahead_y - this_knot_y) <= 1:
            # this_knot touches knot_ahead
            pass
        elif knot_ahead_x == this_knot_x and knot_ahead_y > this_knot_y:
            # in same row, knot ahead above
            this_knot_y += 1
        elif knot_ahead_x == this_knot_x and knot_ahead_y < this_knot_y:
            # in same row, knot ahead below
            this_knot_y -= 1
        elif knot_ahead_y == this_knot_y and knot_ahead_x > this_knot_x:
            # in same row, knot ahead to the right
            this_knot_x += 1
        elif knot_ahead_y == this_knot_y and knot_ahead_x < this_knot_x:
            # in same row, knot ahead to the left
            this_knot_x -= 1
        elif knot_ahead_y - this_knot_y == 1 and knot_ahead_x - this_knot_x == 2:
            #print('a')
            this_knot_x += 1
            this_knot_y += 1
        elif knot_ahead_y - this_knot_y == 1 and knot_ahead_x - this_knot_x == -2:
           # print('b')
            this_knot_x -= 1
            this_knot_y += 1
        elif knot_ahead_y - this_knot_y == -1 and knot_ahead_x - this_knot_x == 2:
           # print('c')
            this_knot_x += 1
            this_knot_y -= 1
        elif knot_ahead_y - this_knot_y == -1 and knot_ahead_x - this_knot_x == -2:
           # print('d')
            this_knot_x -= 1
            this_knot_y -= 1
        elif knot_ahead_y - this_knot_y == 2 and knot_ahead_x - this_knot_x == 1:
            #print('e')
            this_knot_x += 1
            this_knot_y += 1
        elif knot_ahead_y - this_knot_y == -2 and knot_ahead_x - this_knot_x == 1:
           # print('f')
            this_knot_x += 1
            this_knot_y -= 1
        elif knot_ahead_y - this_knot_y == 2 and knot_ahead_x - this_knot_x == -1:
            #print('g')
            this_knot_x -= 1
            this_knot_y += 1
        elif knot_ahead_y - this_knot_y == -2 and knot_ahead_x - this_knot_x == -1:
            #print('h')
            this_knot_x -= 1
            this_knot_y -= 1
        elif knot_ahead_y - this_knot_y == 2 and knot_ahead_x - this_knot_x == 2:
            #print('e')
            this_knot_x += 1
            this_knot_y += 1
        elif knot_ahead_y - this_knot_y == -2 and knot_ahead_x - this_knot_x == 2:
           # print('f')
            this_knot_x += 1
            this_knot_y -= 1
        elif knot_ahead_y - this_knot_y == 2 and knot_ahead_x - this_knot_x == -2:
            #print('g')
            this_knot_x -= 1
            this_knot_y += 1
        elif knot_ahead_y - this_knot_y == -2 and knot_ahead_x - this_knot_x == -2:
            #print('h')
            this_knot_x -= 1
            this_knot_y -= 1
        knots[i+1].locs.append(Coords(this_knot_x, this_knot_y))
    #printable_grid(knots)
print('Part 1:',  len(set(knots[1].locs)))
print('Part 2:', len(set(knots[-1].locs)))
