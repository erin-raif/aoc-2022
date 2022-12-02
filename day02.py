# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 06:59:01 2022

@author: eraif
"""
import numpy as np
import pandas as pd

lines = open('day02.txt','r').read().split('\n')
#lines = ['A Y', 'B X', 'C Z'] # To test with

choice_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_scores = {'loss': 0, 'draw': 3, 'win': 6}
opponent_choices = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
guide = pd.read_csv('day02_rps_guide.csv')

# Part 1
my_choices = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
round_scores = []

for l in lines:
    opponent = opponent_choices[l[0]]
    me = my_choices[l[-1]]
    round_details = guide[(guide['opp'] == opponent) & (guide['me'] == me)]
    outcome = round_details['outcome'].values[0]
    round_score = choice_scores[me] + outcome_scores[outcome]
    round_scores.append(round_score)

print('Part 1 total:', np.sum(round_scores))

# Part 2
strategies = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}
perfect_rounds = []
for l in lines:
    opponent = opponent_choices[l[0]]
    strat = strategies[l[-1]]
    round_details = guide[(guide['opp'] == opponent) & (guide['outcome'] == strat)]
    my_choice = round_details['me'].values[0]
    round_score = choice_scores[my_choice] + outcome_scores[strat]
    perfect_rounds.append(round_score)
print('Part 1 total:', np.sum(perfect_rounds))