# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 07:16:30 2022

@author: eraif
"""

import numpy as np

all_elves = open('day01.txt','r').read().split('\n\n')

elf_sums = []
# for elf in all_elves:
#     e_sum = np.sum(np.array(elf.split('\n'),dtype='int'))
#     elf_sums.append(e_sum)

# elf_sums = np.array(elf_sums)    

# print(np.max(elf_sums))

# sorting = np.argsort(elf_sums)
# sorted_elf_sums = elf_sums[sorting]
# print(sorted_elf_sums[-3:])
# print(np.sum(sorted_elf_sums[-3:]))