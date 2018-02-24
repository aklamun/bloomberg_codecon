# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:12:27 2017

@author: ariahklages-mundt
"""

import math

N = 42

upper_bound = int(math.ceil((N/3)**(1/2.)))

for i in range(upper_bound):
    i2 = i*i
    j = i
    k = int(math.floor((N-i2)**(1/2.)))
    
    while j <= k:
        j2 = j*j
        k2 = k*k
        s = i2+k2+j2
        
        if s < N:
            j+= 1
        elif s > N:
            k-= 1
            
        else:
            break
        break
        
print(i+j+k)