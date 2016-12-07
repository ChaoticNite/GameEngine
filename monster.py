# Monster.py
# Thorin Schmidt
# Edited by Noel Kling
# 11/16/2016

''' CHANGELOG: (11/30/16)
    Adding pieces from the NameGene as individually classes so the generator
    uses several different types of outcomes, will involve a sparing option
    depending on attitude and monster.
    12/06/2016
    NOTE: Got to remember to update CHANGELOGs more often.
    Transferring creatures over from NameGene.py to be more compatible with any
    future updates to the rest of the code. Added the ability for some creatures
    to steal (take) healing potions from the player. Spare function is being added
    to certain creatures based Intelligence.'''


''' Monster Package '''
from namegene import *
from character import *
from random import randint, choice

class Monster(Character):
    ''' generic monster class '''
    def __init__(self,
                 name = "Generic Foe",
                 maxHealth = 10,
                 speed = 25,
                 stamina = 25,
                 strength = 8,
                 dexterity = 8,
                 constitution = 10,
                 intelligence = 8,
                 wisdom = 10,
                 charisma = 10,
                 numberOfPotions = 2,
                 inventory = [],
                 aggression = 50,
                 awareness = 50,
                 fear = 50,
                 imageFileName = "Blob.gif",
                 spRate = 0):
        super(Monster, self).__init__(name, maxHealth, speed, stamina,
                                      strength, dexterity, constitution,
                                      intelligence, wisdom, charisma,
                                      numberOfPotions, inventory, imageFileName,
                                      spRate)
        self.aggression = aggression
        self.awareness = awareness
        self.fear = fear  #indicates cowardice level

        #adject, species = ngName.split(' ')

    def combat_choice(self):
        ''' combat AI

            returns a, h, or f.  Based on aggression, awareness, morale
            
            '''
               
        
        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness
        fleeValue = randint(1,100) + self.fear

        if attackValue >= healValue and attackValue >= fleeValue:
            return "a"
        elif healValue >= attackValue and healValue >= fleeValue:
            return "h"
        elif fleeValue >= attackValue and fleeValue >= healValue:
            return "f"
        else:
            return "AI_error"

class Orc(Monster):
    ''' generic Orc class

        this class '''
    def __init__(self, name = "Dorque da Orc"):
        orcName = name
        maxHealth = randint(1,8)
        speed = 25
        stamina = 25
        strength = randint(8,10)
        dexterity = randint(10,12)
        constitution = 10
        intelligence = 8
        wisdom = 10
        charisma = 10
        numberOfPotions = 2
        inventory = []
        aggression = 80
        awareness = 30
        fear = 20
        super(Orc, self).__init__(orcName, maxHealth, speed, stamina, strength,
                                  dexterity, constitution, intelligence,
                                  wisdom, charisma, numberOfPotions,
                                  inventory, aggression, awareness, fear)
class Moblin(Character):
    
    ''' a greedy violent creature ''' 
    def __init__(self, firstPart = " ", name = "Moblin"):
        moblinName = fristPart + name
        speed = 25
        stamina = 25
        strength = 8
        intelligence = 8
        dexterity = 8
        numberOfPotions = 2
        inventory = []
        aggression = 80
        awareness = 30
        fear = 20
        risk = 20
        maxHealth = 100
        spRate = 0
        super(Moblin, self).__init__(moblinName, maxHealth, speed, stamina,
                                     strength, dexterity, intelligence,
                                     numberOfPotions,
                                     aggression, awareness, fear, risk, spRate)

    def combat_choice(self):
        ''' combat AI

            returns a, h, t, or f. Based on aggression, awareness, morale
            and intelligence.'''
            
        if intellinge > 8:
            if awareness > 50:
                stealValue = randint(1,100) + self.risk
        else:
            stealValue = 0

        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness
        fleeValue = randint(1,100) + self.fear
            
        if attackValue >= healValue and attackValue >= fleeValue and\
            attackValue >= stealValue:
            return "a"
        elif stealValue >= attackValue and stealValue >= healValue and\
              stealValue >= fleeValue:
            return "t"
        elif healValue >= attackValue and healValue >= fleeValue and\
              healValue >= stealValue:
            if self.numberOfPotions > 0:
                return "h"
            else:
                return "t"
        elif fleeValue >= attackValue and fleeValue >= healValue and\
              fleeValue >= stealValue:
            return "f"
        else:
            return "AI_error"
                    
class Minotaur(Character):

    ''' A Heavy Hitting type monster. '''
    def __init__(self, firstPart = " ", name = "Minotaur"):
        minoName = fristPart + name
        speed = 50
        stamina = 40
        strength = 15
        intelligence = 2
        dexterity = 9
        numberOfPotions = 1
        inventory = []
        aggression = 95
        awareness = 60
        fear = 10
        maxHealth = 60
        spRate = 0
        super(Minotaur, self).__init__(name, minoName, maxHealth, speed, stamina,
                                       strength, dexterity, intelligence,
                                       numberOfPotions,
                                       aggression, awareness, fear, spRate)

    def combat_choice(self):
        ''' Combat AI for Minotaur

            Minotaurs are not know to be cowards and would never back down
            from a fight.'''

        
        attackValue = randint(1,100) + self.aggression
        healValue = randint(1,100) + self.awareness

        if attackValue >= healValue and attackValue >= fleeValue:
            return "a"
        elif healValue >= attackValue and healValue >= fleeValue:
            return "h"
        else:
            return "AI_error"

class Raptor(Character):

    ''' An intelligent creature that just happens to be a talking dinosaur.'''
    def __init__(self, firstPart = " ", name = "Raptor"):
        rapName = firstPart + name
        speed = 42
        stamina = 30
        strength = 8
        intelligence = 12
        dexterity = 5
        numberOfPotions = 0
        inventory = []
        aggression = 92
        awareness = 60
        fear = 10
        mercy = 20
        maxHealth = 60
        spare = randint(1,3)
        spRate = 0
        super(Raptor, self).__init__(name, rapName, maxHealth, speed, stamina,
                                       strength, dexterity, intelligence,
                                       numberOfPotions, spare, spRate,
                                       aggression, awareness, fear, mercy)
#    def combat_choice(self):
#        ''' Combat AI for Raptor

#            They are able to be convinced that you aren't worth getting slaughtered.'''
#                
#        attackValue = randint(1,100) + self.aggression
#        healValue = randint(1,100) + self.awareness
#        fleeValue = randint(1,100) + self.fear
#        
#       if spRate < 2:
#            attackValue = attackValue/(spRate/2)
#                return "a"
#            elif healValue >= attackValue and healValue >= fleeValue:
#                return "h"
#            elif fleeValue >= attackValue and fleeValue >= healValue:
#                return "f"
#            else:
#                return "AI_error"
#        elif spRate >= 3:
#            
            
#        elif spRate = 5:
            
            
            


                

def random_monster():
    '''generate a monster at random

    create an instance of each monster here, then add that instance to
    the listOfMonsters.  The function will pick a random instance out of
    the list, then return it to the caller.'''
    
    monster = Monster()
    orc = Orc()
    moblin = Moblin()
    minotaur = Minotaur()
    raptor = Raptor()
    
    
    listOfMonsters = [monster, orc, moblin]
    return choice(listOfMonsters)


if __name__ == "__main__":

    grr = Orc()
    
    #Randy = random_monster(firstPart = ngName, aggression )
    #print(Randy.name)
