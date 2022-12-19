# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 18:46:33 2022

@author: eeenr
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
    
class Sensor:
    def __init__(self, s, b):
        self.s = s
        self.b = b
        self.manhat = manhattan_dist(self.s, self.b)
        return
    def __str__(self):
        return 'Sensor at ' + str(self.s) + '; Beacon at ' + str(self.b) +\
            '; MHD: ' + str(self.manhat)
    def __repr__(self):
        return str(self)
    
class MinMaxPair:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
    def __str__(self):
        return 'Min x: ' + str(self.lo) + ', Max x: ' + str(self.hi) + '\n'
    def __repr__(self):
        return str(self)
    
def manhattan_dist(c1, c2):
    return abs(c1.x - c2.x) + abs(c1.y - c2.y)

def find_forbidden_on_line(line_no, sens):
    dist_to_line = abs(sens.s.y-line_no)
    dist_along_line = sens.manhat - dist_to_line
    if dist_along_line > 0:
        min_x = sens.s.x - dist_along_line
        max_x = sens.s.x + dist_along_line
    else:
        min_x = max_x = sens.s.x
    return min_x, max_x

def get_diamond_path(sens):
    path = [
        [sens.s.x + sens.manhat, sens.s.y],
        [sens.s.x              , sens.s.y + sens.manhat],
        [sens.s.x - sens.manhat, sens.s.y],
        [sens.s.x              , sens.s.y - sens.manhat]
        ]
    return path
details = open('day15.txt').read().split('\n')
sensors = []
for line in details:
    s_det, b_det = line.split(':')
    s_x, s_y = s_det[10:].split(',')
    s_x = int(s_x[2:])
    s_y = int(s_y[3:])
    b_x, b_y = b_det[22:].split(',')
    b_x = int(b_x[2:])
    b_y = int(b_y[3:])
    sensors.append(Sensor(Coords(s_x,s_y),Coords(b_x,b_y)))
    

minmaxes = []
for sens in sensors:
    min_x, max_x = find_forbidden_on_line(2000000, sens)
    if min_x != max_x:
        minmaxes.append([min_x, max_x])
        

minmaxes = np.array(minmaxes, dtype=int)
# Save output for basic off-line processing in Excel which will be quicker than coding
np.savetxt('day15part1.csv', minmaxes, delimiter=',')

fig, ax = plt.subplots()
for sens in sensors:
    path = get_diamond_path(sens)
    print(path)
    ax.add_patch(patches.Polygon(
        path,
        alpha=0.2,
        edgecolor='black',
        facecolor='red'
        ))
ax.set_xlim(0,4000000)
ax.set_ylim(0,4000000)
fig.show()
# Using visualisation, quick to see that the empty spot is at
# x = 3204400, y = 3219131