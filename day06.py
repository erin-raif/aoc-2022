# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 07:21:53 2022

@author: eeenr
"""
from collections import Counter
 
 
def unique_chars(string):
 
    # Counting frequency
    freq = Counter(string)
 
    if(len(freq) == len(string)):
        return True
    else:
        return False

def find_start_marker(signal, length):
    for i in range(len(signal)-length):
        sub = signal[i:i+length]
        if unique_chars(sub):
            return i + length
    
signal = open('day06.txt').read()

p1 = find_start_marker(signal, 4)
print('Part 1:', p1)
p2 = find_start_marker(signal, 14)
print('Part 2:', p2)

