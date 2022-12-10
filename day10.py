# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:58:38 2022

@author: eeenr
"""
import numpy as np

instructions = open('day10.txt').read().split('\n')
#instructions = open('day10test.txt').read().split('\n')

time = 0
register = 1
sig_strengths = []

register_during_cycle = []
for i in instructions:
    if i == "noop":
        register_during_cycle.append(register)
        time += 1
        if time % 40 == 20:
            sig_strengths.append(time*register)
    else:
        register_during_cycle.append(register)
        time += 1
        if time % 40 == 20:
            sig_strengths.append(time*register)
        
        register_during_cycle.append(register)
        time += 1
        if time % 40 == 20:
            sig_strengths.append(time*register)
        register += int(i[5:])
        
print('Part 1 answer:',np.sum(sig_strengths))

screen = []
for position, register in enumerate(register_during_cycle):
    if register-1 <= position % 40 <= register+1:
        screen.append('#')
    else:
        screen.append('.')
        
screen = np.array(screen,dtype=str).reshape(6,40)
np.savetxt('day10out.csv',screen,fmt='%s',delimiter=',')
print('Part 2 outputted to CSV')

