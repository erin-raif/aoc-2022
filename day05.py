# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 07:23:58 2022

@author: eeenr
"""

start_data, instructions = open('day05.txt').read().split('\n\n')

# start_data = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 """

# instructions = """move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

class Instruction:
    def __init__(self, line):
        line = line.split()
        self.n_boxes = int(line[1])
        self.col_from = int(line[3])
        self.col_to = int(line[5])
        
class All_Stacks:
    def __init__(self, n_stacks=9):
        self.n_stacks = n_stacks
        self.stack_list = [[] for x in range(n_stacks)]
        
    def print_me(self):
        for i in range(self.n_stacks):
            print('Stack', i+1,':', self.stack_list[i])
            
    def move(self,how_many, c_from, c_to, rev):
        to_move = self.stack_list[c_from-1][-how_many:]
        if rev: # true for part 1
            to_move.reverse()
        self.stack_list[c_to-1] = self.stack_list[c_to-1] + to_move
        self.stack_list[c_from-1] = self.stack_list[c_from-1][:-how_many]

        
all_inst = []

for i in instructions.split('\n'):
    print(i)
    all_inst.append(Instruction(i))

start_data = start_data.split('\n')
no_stacks = int(start_data[-1].split('   ')[-1][0])
print(no_stacks)

all_stacks = All_Stacks(no_stacks)

for line in reversed(start_data[:-1]):
    for i in range(no_stacks):
        box = line[4*i:4*i+3]
        if box != '   ':
            all_stacks.stack_list[i].append(box)
            
for inst in all_inst:
    all_stacks.move(inst.n_boxes, inst.col_from, inst.col_to, False)

all_stacks.print_me()
