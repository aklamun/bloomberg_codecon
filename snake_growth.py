# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:49:29 2016

@author: ariahklages-mundt
"""

import operator
from copy import deepcopy

data = ['2 3', '4', '0 1', '0 2', '1 2', '1 1', '8', 'R', 'R', 'D', 'L', 'U', 'R', 'D', 'L']
rows, cols = data[0].split(' ')
rows = int(rows)
cols = int(cols)
fn = int(data[1])
food_locs = []
moves = []
for i in range(2,fn+2):
    r, c = data[i].split(' ')
    r = int(r)
    c = int(c)
    food_locs.append((r,c))
mn = int(data[fn+2])
for i in range(fn+3,mn+fn+3):
    moves.append(data[i])

snake_cells = [(0,0)]
count = 0
for move in moves:
    count = count + 1
    snake_cells_new = []
    a = snake_cells[0] 
    if move == 'U':
        #format is (row, column)
        b = (-1, 0)
    elif move == 'R':
        b = (0, 1)
    elif move == 'L':
        b = (0, -1)
    elif move == 'D':
        b = (1, 0)
    snake_cells_new.append(tuple(map(operator.add, a, b)))
    for i in range(len(snake_cells)-1):
        snake_cells_new.append(snake_cells[i])
    if snake_cells_new[0] in food_locs:
        snake_cells_new.append(snake_cells[-1])
        food_locs.remove(snake_cells_new[0])
    snake_cells = deepcopy(snake_cells_new)
    if snake_cells[0] in snake_cells[1:]:
        answer = count
        break
    elif move == moves[-1]:
        answer = -1
    
        
                