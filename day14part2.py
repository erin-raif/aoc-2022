# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:41:42 2022

@author: eeenr
"""

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __eq__(self,c):
        return self.x == c.x and self.y == c.y
    def __hash__(self):
        return hash(str(self))


class Grid:
    def __init__(self, walls):
        self.filled_coords = set([])
        for wall in walls:
            coords = wall.split(' -> ')
            cs = []
            for c in coords:
                x, y = c.split(',')
                cs.append(Coords(int(x),int(y)))
            for i in range(len(cs)-1):
                self.draw_line(cs[i],cs[i+1])
        self.floor = max([c.y for c in self.filled_coords]) + 2
        self.sand_count = 0
        return
                
    def draw_line(self,c1,c2):
        if c1.x == c2.x and c2.y > c1.y:
            for y in range(abs(c2.y-c1.y)+1):
                self.filled_coords.add(Coords(c1.x,c1.y+y))
        elif c1.x == c2.x and c2.y < c1.y:
            for y in range(abs(c2.y-c1.y)+1):
                self.filled_coords.add(Coords(c1.x,c1.y-y))
        elif c1.y == c2.y and c2.x > c1.x:
            for x in range(abs(c2.x-c1.x)+1):
                self.filled_coords.add(Coords(c1.x+x,c1.y))
        elif c1.y == c2.y and c2.x < c1.x:
            for x in range(abs(c2.x-c1.x)+1):
                self.filled_coords.add(Coords(c1.x-x,c1.y))
        return
    
    def drop_sand(self):
        current_x = 500
        current_y = 0
        end = False
        on_floor = False
        while not end:
            if current_y + 1 == self.floor:
                end = True
            else:
                if Coords(current_x,current_y+1) not in self.filled_coords:
                    current_y += 1
                elif Coords(current_x-1,current_y+1) not in self.filled_coords:
                    current_y += 1
                    current_x -= 1
                elif Coords(current_x+1,current_y+1) not in self.filled_coords:
                    current_y += 1
                    current_x += 1
                else:
                    end = True
        resting_point = Coords(current_x, current_y)
        self.filled_coords.add(resting_point)
        self.sand_count += 1
        return resting_point

    
lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split('\n')
lines = open('day14.txt').read().split('\n')

g = Grid(lines)
print(g.filled_coords)

resting_point = Coords(0,0) # placeholder

while resting_point != Coords(500,0):
    resting_point = g.drop_sand()
    
print('Part 2 answer:', g.sand_count)

