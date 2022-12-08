# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:32:00 2022

@author: eeenr
"""
import numpy as np

forest = """30373
25512
65332
33549
35390""".split('\n')
forest = open('day08.txt').read().split('\n')

# Add an extra ring of zeros round the side.
# This does not affect the operations but means I don't have
# to handle corner cases.   
forest = [('0' + row + '0') for row in forest]

zero_row = '0' * len(forest[0])
forest.insert(0, zero_row)
forest.append(zero_row)

forest = [[*row] for row in forest]
forest = np.array(forest, dtype=int)

# access with [y-coord, x-coord]
row_len = len(forest[0])
col_len = len(forest[:,0])

# Create blank arrays for both parts
visible = np.zeros_like(forest,dtype='bool')
scenic_score = np.zeros_like(forest,dtype=int)
for j in range(2,col_len-2):
    for i in range(2, row_len-2):
        height = forest[j,i]
        # Part 1 loop - check if visible from edge
        if height > forest[:j,i].max():
            visible[j,i] = True
        elif height > forest[j+1:,i].max():
            visible[j,i] = True
        elif height > forest[j,:i].max():
            visible[j,i] = True
        elif height > forest[j,i+1:].max():
            visible[j,i] = True
        # Part 2 loop - get trees visible in each direction from each spot
        # note that order flipped when looking up and left
        up = np.flip(forest[1:j,i])
        down = forest[j+1:-1,i]
        left = np.flip(forest[j,1:i])
        right = forest[j,i+1:-1]
        all_dirs = [up, down, left, right]
        ss_dirs = []
        # get number of visible trees in direction
        for d in all_dirs:
            if height > d.max():
                visible_trees = len(d)
            else:
                visible_trees = 1
                for k in d.tolist():
                    if k < height:
                        visible_trees += 1
                    else:
                        break
            ss_dirs.append(visible_trees)
        scenic_score[j,i] = np.product(ss_dirs)
        
# Handle forest edges
for j in range(1,col_len-1):
    visible[j,1] = True
    visible[j,-2] = True

for i in range(1,row_len-1):
        visible[1,i] = True
        visible[-2,i] = True

count = np.count_nonzero(visible == True)
print('Part 1 answer:', count)
print('Part 2 answer:',scenic_score.max())
            
