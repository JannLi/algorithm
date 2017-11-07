# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 15:17:49 2017

@author: JANN
"""

import sys
try: 
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break 
        lines = line.split()
        print int(lines[0]) + int(lines[1])
except: 
    pass