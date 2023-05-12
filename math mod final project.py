# -*- coding: utf-8 -*-
"""
Created on Thu May 11 18:54:52 2023

@author: kylem
"""

# =============================================================================
# Andrew K and Kyle M
# =============================================================================


mass = 8.34 #this is the weight of water per gallon
#this weight per gal will give us the a similar result since waste is mostly water

days = 28

#28 days for all to get each tank below 1%
#49 for less than 0.1% which is basically 0

tank1=137600/mass #gallons of sewage
t1max = tank1     #starting amount
t1current = tank1 #current amount
t1=False

tank2= 22800/mass
t2max = tank2
t2current = tank2
t2=False

tank3=44020/mass
t3max = tank3
t3current = tank3
t3=False

count = 0


while count < (days)*8 :#21 times 8 cuz 8 hours in a work day
    t1current = tank1
    t2current = tank2
    t3current = tank3
    
    #tank
    
    
    if tank1 > 1:
        tank1 = tank1 + ((135*(t2current/t2max))-(370*(t1current/t1max)))
    if tank1 <=1376:
        print('tank1 done at ', count/8, tank1)
        t1=True
    
    if tank2 > 1:
        tank2 = tank2 + (370*(t1current/t1max) + 85*(t3current/t3max) - (135+320)*(t2current/t2max))
    if tank2 <= 228:
        print('tank2 done at', count/8, tank2)
        t2=True
        
    if tank3 > 1:
        tank3 = tank3 + ((320*(t2current/t2max)) - (85+235)*(t3current/t3max))
    if tank3 <= 441:
        print('tank3 dont at ', count/8, tank3)
        t3=True
        
    #if t1 == t2 == t3 == True:
    #    break
    count+=1
    
    
print('t1', tank1/t1max)
print('t2', tank2/t2max)
print('t3', tank3/t3max)
