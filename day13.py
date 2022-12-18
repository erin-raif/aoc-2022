# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:48:02 2022

@author: eeenr
"""

class Pair:
    def __init__(self, pair_in, index):
        #self.left = []
        #self.right = []
        left, right = pair_in.split('\n')
        self.left = eval(left)
        self.right = eval(right)
        self.index = index
        self.correct = compare_lists(self.left, self.right)
        return
    
    def __repr__(self):
        return 'Pair ' + str(self.index) + ' ' + str(self.correct)
    
class Signal:
    def __init__(self, string):
        self.sig = eval(string)
    
    def __lt__(self, s2):
        return compare_lists(self.sig, s2.sig)
    
    def __gt__(self, s2):
        return not compare_lists(self.sig, s2.sig)
    
    def __repr__(self):
        return str(self.sig)
    
    def __eq__(self, s):
        return self.sig == s.sig
                    
def compare_lists(left, right):
    for n, l_item in enumerate(left):
        if n >= len(right):
            return False
        if l_item == right[n]:
            pass
        elif type(l_item) == int and type(right[n]) == int:
            #both are ints
            if l_item < right[n]:
                return True
            elif l_item > right[n]:
                return False
        else:
            # at least one is a list
            if type(l_item) == int:
                comp = compare_lists([l_item],right[n])
            elif type(right[n]) == int:
                comp = compare_lists(l_item,[right[n]])
            else:
                comp = compare_lists(l_item,right[n])
            if comp != None:
                return comp
    if len(left) < len(right):
        return True
    else:
        return None
# Part 1
all_lists = open('day13.txt').read().split('\n\n')

pairs = [Pair(p, i+1) for i, p in enumerate(all_lists)]

correct_pair_sum = 0
for p in pairs:
    if p.correct:
        correct_pair_sum += p.index
        
print('Part 1 Answer:', correct_pair_sum)
# Part 2
all_signals = open('day13.txt').read().split('\n')
signals = []
for s in all_signals:
    if len(s) >= 2: # avoid empty lines
        signals.append(Signal(s))
signals.append(Signal('[[2]]'))
signals.append(Signal('[[6]]'))

signals = sorted(signals)
loc2 = signals.index(Signal('[[2]]')) + 1
loc6 = signals.index(Signal('[[6]]')) + 1

print('Part 2 Answer:', loc2*loc6)