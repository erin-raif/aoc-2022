# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 06:50:20 2022

@author: eeenr
"""

import re
import numpy as np

def all_slashes(st):    
    slashes = [m.start() for m in re.finditer('/', st)]
    return slashes

class directory:
    def __init__(self, name, level):
        self.dname = name
        self.files = []
        self.subdirs = []
        self.level = level
    def add_subdir(self,subdir):
        self.subdirs.append(subdir)
    def add_files(self, file):
        self.files.append(file)
    def get_size(self, all_sizes):
        # Recursively search within directory to get dir size
        dsize = 0
        for d in self.subdirs:
            this_d_size, all_sizes = d.get_size(all_sizes)
            dsize += this_d_size
        for f in self.files:
            dsize += int(f.fsize)
        all_sizes.append(dsize)
        return dsize, all_sizes
    def find_subdir_index(self, sub_name):
        for i in range(len(self.subdirs)):
            if self.subdirs[i].dname == sub_name:
                return i
    # For debugging
    def print_name(self):
        print('    Name: ' + self.dname + '; level: ' + str(self.level))

    def print_me_2(self):
        print('Name: ' + self.dname + '; level: ' + str(self.level))
        print('Subdirectories:')
        for d in self.subdirs:
            d.print_name()
        print('Files: ')
        for f in self.files:
            print(f)
    
    
class file:
    def __init__(self, name, fsize, level):
        self.fname = name
        self.fsize = fsize
        self.level = level
    def __str__(self):
        # Good debugging practice (impractical for directory)
        return '-' * self.level + ' ' + self.fname + '\t\t\ts=' + str(self.fsize)
    
commands = open('day07.txt').read().split('\n')
#commands = open('day07test.txt').read().split('\n')

full_loc = '/'
# Create top level directory
top_dir = directory('/',0)
# Use current dir as a handle that can be exchanged.
current_dir = top_dir
for c in commands[1:]:
    if c[0] == '$':
        if c[2:4] == 'cd' and c[-2:] == '..':
            # Move backwards
            slashes = all_slashes(full_loc)
            # find parent directory using the full location string
            # and attach to current dir handle
            all_dirs = full_loc.split('/')
            temp_dir = top_dir
            for d in all_dirs[1:-1]:
                temp_dir_ind = temp_dir.find_subdir_index(d)
                temp_dir = temp_dir.subdirs[temp_dir_ind]
            current_dir = temp_dir
            if len(slashes) > 1:    
                full_loc = full_loc[:slashes[-1]]
            else:
                full_loc = '/'
            
        elif c[2:4] == 'cd':
            subdir_name =  c[5:]
            slashes = all_slashes(full_loc)
            if full_loc == '/':
                full_loc = full_loc + subdir_name
            else:
                full_loc = full_loc + '/' + subdir_name
            subdir_index = current_dir.find_subdir_index(subdir_name)
            current_dir = current_dir.subdirs[subdir_index]
                
        elif c[2:4] == 'ls':
            pass
        
    elif c[0:3] == 'dir':
        # add directory
        slashes = all_slashes(full_loc)
        level = len(slashes)
        if full_loc == '/':    
            current_dir.add_subdir(directory(c[4:],level))
        else:
            current_dir.add_subdir(directory(c[4:],level+1))
    elif c[0].isnumeric():
        # add file
        size, name = c.split()
        level = len(slashes)
        if full_loc == '/':    
            current_dir.add_files(file(name, size, level))
        else:
            current_dir.add_files(file(name, size, level+1))

total, all_s = top_dir.get_size([])
all_s = np.array(all_s)
masked = np.ma.masked_greater(all_s, 100000)
print('Part 1 Answer:', masked.sum())
masked2 = np.ma.masked_less(all_s, total-40000000)
print('Part 2 Answer:', masked2.min())
    
         