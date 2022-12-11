# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 07:29:16 2022

@author: eraif
"""

import numpy as np

monkey_data = open('day11test.txt').read().split('\n\n')

class Monkey():
    def __init__(self, ID, start_vals, test_divisor, true_throw, false_throw):
        self.ID = ID
        self.items = start_vals
        self.test_divisor = test_divisor
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspection_count = 0
        self.mod_items = []
        return
    def play_operation(self, item):
        return item    
    def play_with_item(self,item, all_monkeys):
        operation_detail = 'Monkey ' + str(self.ID) + ' had item with worry level '\
            + str(item) + '.'
        item = self.play_operation(item)//3
        operation_detail = operation_detail + 'This became ' + str(item) + \
            ' after the inspection. It was thrown to Monkey '
        if item % self.test_divisor == 0:
            all_monkeys[self.true_throw].catch_item(item)
            operation_detail = operation_detail + str(self.true_throw)
        else:
            all_monkeys[self.false_throw].catch_item(item)
            operation_detail = operation_detail + str(self.false_throw)
        #print(operation_detail)
        self.inspection_count += 1
        return
    def play_with_all_items(self, all_monkeys):
        for item in self.items:
            self.play_with_item(item, all_monkeys)
        self.items = []
        return
    def catch_item(self, item):
        self.items.append(item)
        return
    def op_str(self):
        return 'No op'
    def __repr__(self):
        pt1 = 'Monkey ' + str(self.ID)
        pt2 = '  Items: '
        for i in self.items:
            pt2 = pt2 + str(i) + ' '
        pt3 = '  Test: divisible by ' + str(self.test_divisor)
        pt4 = self.op_str()
        pt5 = '    If true, throw to Monkey ' + str(self.true_throw)
        pt6 = '    If false, throw to Monkey ' + str(self.false_throw)
        pt7 = '  Current inspection count: ' + str(self.inspection_count)
        return pt1 + '\n' + pt2 + '\n' + pt3 + '\n' + pt4 + '\n' +  \
                pt5 + '\n' +  pt6 + '\n' +  pt7
    
class AddingMonkey(Monkey):
    def __init__(self, ID, start_vals, test_divisor, true_throw, false_throw, add_on):
        super().__init__(ID, start_vals, test_divisor, true_throw, false_throw)
        self.add_on = add_on
        return
    def play_operation(self, item):
        item += self.add_on
        return item
    def op_str(self):
        return '  Operation: new = old + ' + str(self.add_on)
    
class MultiplyingMonkey(Monkey):
    def __init__(self, ID, start_vals, test_divisor, true_throw, false_throw, times_by):
        super().__init__(ID, start_vals, test_divisor, true_throw, false_throw)
        self.times_by = times_by
        return
    def play_operation(self, item):
        item *= self.times_by
        return item
    def op_str(self):
        return '  Operation: new = old * ' + str(self.times_by)

class SquaringMonkey(Monkey):
    def __init__(self, ID, start_vals, test_divisor, true_throw, false_throw):
        super().__init__(ID, start_vals, test_divisor, true_throw, false_throw)
        return
    def play_operation(self, item):
        item = item ** 2
        return item
    def op_str(self):
        return '  Operation: new = old * old'
        
all_monkeys = []

for m in monkey_data:
    m = m.split('\n')
    ID = int(m[0][-2])
    items = [int(i) for i in m[1][18:].split(', ')]
    divisor = int(m[3][20:])
    true_t = int(m[4][-1])
    false_t = int(m[5][-1])
    if 'old * old' in m[2]:
        all_monkeys.append(SquaringMonkey(ID, items, divisor, true_t, false_t))
    elif '*' in m[2]:
        times_by = int(m[2][24:])
        all_monkeys.append(MultiplyingMonkey(ID, items, divisor, true_t, false_t, times_by))
    else:
       # adding 
       add_on = int(m[2][24:])
       all_monkeys.append(AddingMonkey(ID, items, divisor, true_t, false_t, add_on))


for i in range(20):
    for m in all_monkeys:
        m.play_with_all_items(all_monkeys)
     

insp_count = [m.inspection_count for m in all_monkeys]
insp_count = np.sort(insp_count)
print('Part 1 answer:', insp_count[-1]*insp_count[-2])
