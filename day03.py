# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:10:41 2022

@author: eraif
"""
import string

letters = string.ascii_letters

rucksacks = open('day03.txt','r').read().split('\n')

# rucksacks = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".split('\n')

sum_duplicate_priorities = 0
for sack in rucksacks:
    items = len(sack)
    comp1 = set(sack[:len(sack)//2])
    comp2 = set(sack[len(sack)//2:])
    duplicate = list(comp1.intersection(comp2))[0]
    priority = letters.index(duplicate) + 1
    sum_duplicate_priorities += priority

print('Part 1 answer:', sum_duplicate_priorities)

sum_badge_priorities = 0
for i in range(len(rucksacks)//3):
    sack1 = set(rucksacks[3*i])
    sack2 = set(rucksacks[3*i+1])
    sack3 = set(rucksacks[3*i+2])
    badge = list(sack1.intersection(sack2, sack3))[0]
    sum_badge_priorities += letters.index(badge) + 1

print('Part 2 answer:', sum_badge_priorities)
    
    