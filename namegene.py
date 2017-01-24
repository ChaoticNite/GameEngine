# !/usr/bin/python3
# namegene.py
# Noel Kling
# November/17/16

import random
from random import randint

adjectName = ["Kind", "Average", "Lazy", "Noble", "Aggressive", "Boss",
             "Zesty", "Unbeatable"]
namePart = random.randint(1, 8)
ngAggression = 0
ngSpeed = 0
ngAwareness = 0
ngFear = 0
ngIntelligence = 0
       
if namePart == 1:
    firstPart = adjectName[0]
    ngAggression =  -10
        
elif namePart == 2:
    firstPart = adjectName[1]
        
elif namePart == 3:
    firstPart = adjectName[2]
    ngSpeed = ngSpeed - randint(5,10)
    ngAggression = ngAggression - randint(15,20)
    ngAwareness = ngAwareness - randint(15,20)
    ngFear = ngFear - randint(15,20)
        
elif namePart == 4:
    firstPart = adjectName[3]
    ngAggression = ngAggression + randint(5, 10)
    ngAwareness = ngAwareness + randint(15, 20)
    ngFear = ngFear - randint(5, 15)
        
elif namePart == 5:
    firstPart = adjectName[4]
    ngAggression = ngAggression + randint(15, 25)
    ngAwareness = ngAwareness - randint(10, 20)
    ngFear = ngFear - 5
        
elif namePart == 6:
    firstPart = adjectName[5]
    ngIntelligence = ngIntelligence + 10
    ngAggression = ngAggression + 10
    ngAwareness = ngAwareness + 10
    ngFear = ngFear - 10
        
elif namePart == 7:
    firstPart = adjectName[6]
    ngAggression = ngAggression + randint(-20, 20)
    ngAwareness = ngAwareness + randint(-10, 10)
    ngFear = ngFear + randint(-5, 5)
        
elif namePart == 8:
    firstPart = adjectName[7]
    ngAggression = ngAggression + 20
    ngAwareness = ngAwareness + 20
    ngFear = ngFear - randint(5, 15)

ngName = firstPart
