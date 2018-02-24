# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:26:11 2016

@author: ariahklages-mundt
"""

data = ['12', '^A', '3', '^B', '2', '^C', '/B', '/C', '-1', '^B', '4', '/A', '/B']

#Problem        : Minimum Sets
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

data = sys.stdin.read().splitlines()

sets = []
sets_open = {}
sets_dict = {}

for line in data[1:]:
    if line[0] == '^':
        set_name = line[1]
        if set_name not in sets:
            sets.append(set_name)
            sets_dict[set_name] = []
        sets_open[set_name] = 1
    elif line[0] == '/':
        set_name = line[1]
        sets_open[set_name] = 0
    else:
        for set_name in sets:
            if sets_open[set_name] == 1:
                s = sets_dict[set_name]
                s.append(int(line))
                sets_dict[set_name] = s
sets.sort()
for set_name in sets:
    line = set_name
    s = sets_dict[set_name]
    s.sort()
    for n in s:
        line = line + " " + str(n)
    print(line)

