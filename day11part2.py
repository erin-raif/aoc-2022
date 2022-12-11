# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:38:32 2022

@author: eraif
"""

monkey_data = open('day11.txt').read().split('\n\n')

class ModItem():
    def __init__(self, value, mods):
        self.mods = {}
        for m in mods:
            self.mods[m] = value % m
    def increment_mods(self, inc):
        # y = nq + r, y mod n = r
        # y + k = nq + r + k, y + k mod n = (r + k) mod n
        for m in self.mods:
            self.mods[m] = (self.mods[m] + inc) % m
        return
    def square_mods(self):
        #  y = nq + r,          y mod n = r mod n = r
        #y^2 = nq(nq+2r) + r^2, y^2 mod n = r^2 mod n
        for m in self.mods:
            # hack for squaring
            self.mods[m] = (self.mods[m]**2) % m
        return
    def multiply_mods(self, coeff):
        #  y = nq + r,   y mod n = r mod n = r
        # ky = knq + kr, ky mod n = kr mod n
        for m in self.mods:
            self.mods[m] = (self.mods[m]*coeff) % m
        return
    def __str__(self):
        base = 'Item with:\n'
        for m in self.mods:
            base = base + '    mod ' + str(m) + ' = ' + str(self.mods[m]) + '\n'
        return base
    def __repr__(self):
        return self.__str__()

class Monkey():
    def __init__(self, ID, items, test_divisor, true_throw, false_throw):
        self.ID = ID
        self.items = items
        self.test_divisor = test_divisor
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspection_count = 0
        return
    def play_with_item(self, item, all_monkeys):
        if item.mods[self.test_divisor] == 0:
            all_monkeys[self.true_throw].catch_item(item)
        else:
            all_monkeys[self.false_throw].catch_item(item)
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

class AddMonkey(Monkey):
    def __init__(self, ID, items, test_divisor, true_throw, false_throw, mod_inc):
        super().__init__(ID, items, test_divisor, true_throw, false_throw)
        self.mod_inc = mod_inc
        return
    def play_with_item(self, item, all_monkeys):
        item.increment_mods(self.mod_inc)
        super().play_with_item(item, all_monkeys)
        return

class TimesMonkey(Monkey):
    def __init__(self, ID, items, test_divisor, true_throw, false_throw, coeff):
        super().__init__(ID, items, test_divisor, true_throw, false_throw)
        self.coeff = coeff
        return
    def play_with_item(self, item, all_monkeys):
        item.multiply_mods(self.coeff)
        super().play_with_item(item, all_monkeys)
        return
    
class SquareMonkey(Monkey):
    def __init__(self, ID, items, test_divisor, true_throw, false_throw):
        super().__init__(ID, items, test_divisor, true_throw, false_throw)
        return
    def play_with_item(self, item, all_monkeys):
        item.square_mods()
        super().play_with_item(item, all_monkeys)
        return

all_monkeys = []
mods = []
for m in monkey_data:
    # quick loop to get all mods
    m = m.split('\n')
    mods.append(int(m[3][20:]))

for m in monkey_data:
    m = m.split('\n')
    ID = int(m[0][-2])
    items = [ModItem(int(i),mods) for i in m[1][18:].split(', ')]
    divisor = int(m[3][20:])
    true_t = int(m[4][-1])
    false_t = int(m[5][-1])
    if '+' in m[2]:
        mod_inc = int(m[2][24:])
        all_monkeys.append(AddMonkey(ID, items, divisor, true_t, false_t, mod_inc))
    elif 'old * old' in m[2]:
        all_monkeys.append(SquareMonkey(ID, items, divisor, true_t, false_t))
    else:
        coeff = int(m[2][24:])
        all_monkeys.append(TimesMonkey(ID, items, divisor, true_t, false_t, coeff))


for i in range(10000):
    for m in all_monkeys:
        m.play_with_all_items(all_monkeys)

insp_count = sorted([m.inspection_count for m in all_monkeys])
print('Part 2 answer:', insp_count[-1]*insp_count[-2])
