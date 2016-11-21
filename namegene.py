# !/usr/bin/python3
# namegene.py
# Noel Kling
# November/17/16

from monster import *
import random
from random import randint

adjectName = ["Kind", "Average", "Lazy", "Noble", "Aggressive", "Boss",
             "Zesty", "Unbeatable"]
nameSpecies = ["Moblin", "Minotaur", "Raptor", "Kobold", "Wolysion", "Tarawin"]

class Moblin(Monster):
    ''' a greedy violent creature '''
    def __init__(self,
                 ngName = "da Moblin"
                 ngSpeed = 25
                 ngStamina = 25
                 ngStrength = 8
                 ngIntelligence = 8
                 ngDexterity = 8
                 ngNumberOfPotions = 2
                 ngInventory = []
                 ngAggression = 80
                 ngAwareness = 30
                 ngFear = 20
                 ngMXHealth = 100):
        super(Moblin, self).(ngName, ngMXHealth, ngSpeed, ngStamina, ngStrength,
                             ngIntelligence, ngDexterity, ngNumberOfPotions,
                             ngInventory, ngAggression, ngAwareness, ngFear)

        def combat_choice(self):
            ''' combat AI

                returns a, h, t, or f. Based on aggression, awareness, morale
                and intelligence.

                '''
            if 

            

    


namePart1 = random.randint(1, 8)
namePart2 = random.randint(1, 6)

if namePart2 == 1:
    name2 = nameSpecies[0]
    ngSpeed = 25
    ngStamina = 25
    ngStrength = 8
    ngIntelligence = 8
    ngDexterity = 8
    ngNumberOfPotions = 2
    ngInventory = []
    ngAggression = 80
    ngAwareness = 30
    ngFear = 20
    ngMXHealth = 100
       
elif namePart2 == 2:
    name2 = nameSpecies[1]
    ngSpeed = 50
    ngStamina = 40
    ngStrength = 15
    ngIntelligence = 2
    ngDexterity = 9
    ngNumberOfPotions = 1
    ngInventory = []
    ngAggression = 95
    ngAwareness = 15
    ngFear = 5
    ngMXHealth = 150
        
elif namePart2 == 3:
    name2 = nameSpecies[2]
    ngSpeed = 42
    ngStamina = 30
    ngStrength = 8
    ngIntelligence = 12
    ngDexterity = 5
    ngNumberOfPotions = 0
    ngInventory = []
    ngAggression = 92
    ngAwareness = 60
    ngFear = 10
    ngMXHealth = 60
        
elif namePart2 == 4:
    name2 = nameSpecies[3]
    ngSpeed = 4
    ngStamina = 6
    ngStrength = 2
    ngIntelligence = 4
    ngDexterity = 3
    ngNumberOfPotions = 4
    ngInventory = []
    ngAggression = 50
    ngAwareness = 20
    ngFear = 90
    ngMXHealth = 20
        
elif namePart2 == 5:
    name2 = nameSpecies[4]
    ngSpeed = 12
    ngStamina = 30
    ngStrength = 8
    ngIntelligence = 20
    ngDexterity = 12
    ngNumberOfPotions = 3
    ngInventory = []
    ngAggression = 40
    ngAwareness = 90
    ngFear = 30
    ngMXHealth = 60
        
elif namePart2 == 6:
    name2 = nameSpecies[5]
    ngSpeed = 25
    ngStamina = 25
    ngStrength = 8
    ngIntelligence = 8
    ngDexterity = 8
    ngNumberOfPotions = 2
    ngInventory = []
    ngAggression = 80
    ngAwareness = 30
    ngFear = 20
    ngMXHealth = 40

        
if namePart1 == 1:
    firstPart = adjectName[0]
    ngAggression = ngAggression - 10
        
elif namePart1 == 2:
    firstPart = adjectName[1]
        
elif namePart1 == 3:
    firstPart = adjectName[2]
    ngSpeed = ngSpeed - randint(5,10)
    ngAggression = ngAggression - randint(15,20)
    ngAwareness = ngAwareness - randint(15,20)
    ngFear = ngFear - randint(15,20)
        
elif namePart1 == 4:
    firstPart = adjectName[3]
    ngAggression = ngAggression + randint(5, 10)
    ngAwareness = ngAwareness + randint(15, 20)
    ngFear = ngFear - randint(5, 15)
        
elif namePart1 == 5:
    firstPart = adjectName[4]
    ngAggression = ngAggression + randint(15, 25)
    ngAwareness = ngAwareness - randint(10, 20)
    ngFear = ngFear - 5
        
elif namePart1 == 6:
    firstPart = adjectName[5]
    ngIntelligence = ngIntelligence + 10
    ngAggression = ngAggression + 10
    ngAwareness = ngAwareness + 10
    ngFear = ngFear - 10
        
elif namePart1 == 7:
    firstPart = adjectName[6]
    ngAggression = ngAggression + randint(-20, 20)
    ngAwareness = ngAwareness + randint(-10, 10)
    ngFear = ngFear + randint(-5, 5)
        
elif namePart1 == 8:
    firstPart = adjectName[7]
    ngAggression = ngAggression + 20
    ngAwareness = ngAwareness + 20
    ngFear = ngFear - randint(5, 15)

ngName = firstPart + " " + name2
