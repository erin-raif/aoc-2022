# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 06:48:55 2022

@author: eraif
"""
assignment_lines = open('day04.txt','r').read().split('\n')

total_lines = len(assignment_lines)
part1_count = 0
part2_count = 0

for line in assignment_lines:
    (first, second) = line.split(',')
    first = first.split('-')
    second = second.split('-')
    first_min = int(first[0])
    first_max = int(first[1])
    second_min = int(second[0])
    second_max = int(second[1])
    if first_min <= second_min and first_max >= second_max:
        part1_count += 1
    elif first_min >= second_min and first_max <= second_max:
        part1_count += 1
    if first_max < second_min or second_max < first_min:
        part2_count += 1
        
print('Part 1 Answer', part1_count)
print('Part 2 Answer', total_lines - part2_count)