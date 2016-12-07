# character_creator.py
# Thorin Schmidt
# Edited by Noel Kling
# 11/29/2016

''' GUI-based character generator'''
import tkinter as tk
import character as ch
from monster import *
import random as rd

TITLE_FONT = ("Helvetica", 20, "bold")
HEADING1_FONT = ("Helvetica", 16, "bold")
TABLE_FONT = ("Arial", 14, "bold")
INSTRUCTION_FONT = ("Helvetica", 14, "bold")
SIMPLE_MESSAGE = 'The user is asked which stat(str, dex, con, int, wis, cha) ' + \
                'is most important, and which is least.  most important gets ' + \
                'a value of 17, least gets a 9, and the rest get 12. This method ' + \
                'is suitable for a 20-point character build using Pathfinder d20 ' + \
                'rules.  This method has only a few choices, and results in ' + \
                'moderate satisfaction for the user.'

HARDCORE_MESSAGE = 'results are generated randomly using the 3d6 method, in ' + \
                'standard stat block sequence: (str, dex, con, int, wis, cha). ' + \
                'if none of the stats are over 13, then the entire set is re-' + \
                'rolled until it does. The user has no control over ability ' + \
                'scores. This method is the easiest, but usually has the least ' + \
                'satisfaction for the user.'

FOURD6_MESSAGE = 'keep best three, arrange to suit - 6 sets of 4d6 are rolled, ' + \
                'in each set, the top three dice are kept and added together. ' + \
                'Then these scores are assigned by the user. This method usually ' + \
                'has the highest satisfaction for the player, but is also the ' + \
                'most complicated, due to the many choices required.'
                

class RootApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.player = ch.Character()
        self.columnconfigure(0, weight = 1)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame(self) 
        container.grid_columnconfigure(0, weight=1)
        container.grid(sticky = (tk.N+tk.S+tk.E+tk.W))
        self.frames = {}
        for F in (Menu, Hardcore, Simple, FourD6, Help):
            page_name = F.__name__
            frame = F(parent=container, controller=self) 
            self.frames[page_name] = frame  

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        self.show_frame("Menu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Menu(tk.Frame):
    """ Opening Menu for Character Creator """ 
    def __init__(self, parent, controller):
        """ Initialize the frame. """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight = 1)
        self.grid(sticky = (tk.E+tk.W))
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.instLbl = tk.Label(self, text =
                              "Choose a Character Creation Method:")
        self.instLbl.grid(row = 0, column = 0, sticky = (tk.E+tk.W))

        # create whitespace
        self.blankLbl = tk.Label(self, text = '')
        self.blankLbl.grid(row = 1, column = 0, sticky = (tk.E+tk.W))

        # create hardcore button
        self.hcBttn = tk.Button(self, text = "Hardcore",
                                command = lambda:
                                self.controller.show_frame("Hardcore"))
        self.hcBttn.grid(row = 2, column = 0, sticky = (tk.E+tk.W))

        # create simple button
        self.simpleBttn = tk.Button(self, text = "Simple",
                                    command = lambda:
                                    self.controller.show_frame("Simple"))
        self.simpleBttn.grid(row = 3, column = 0, sticky = (tk.E+tk.W))

        # create 4d6 button
        self.fourD6Bttn = tk.Button(self, text = "4d6",
                                    command = lambda:
                                    self.controller.show_frame("FourD6"))
        self.fourD6Bttn.grid(row = 4, column = 0, sticky = (tk.E+tk.W))

        # create Description button
        self.helpBttn = tk.Button(self, text = "Method Descriptions",
                                  command = lambda:
                                  self.controller.show_frame("Help"))
        self.helpBttn.grid(row = 5, column = 0, sticky = (tk.E+tk.W))

class Hardcore(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        label = tk.Label(self, text="Hardcore", font=TITLE_FONT)
        label.grid(row = 0, column = 1)
        self.roll_dice()
        self.strVar = tk.StringVar()
        self.strVar = self.statBlock[0]
        self.create_widgets()

    def roll_dice(self):
        '''Rolls if none are higher than 11'''
        valid = False
        while not valid:
            self.statBlock = [rd.randint(3,18),
                              rd.randint(3,18),
                              rd.randint(3,18),
                              rd.randint(3,18),
                              rd.randint(3,18),
                              rd.randint(3,18)]
            if self.statBlock[0] > 11 or self.statBlock[1] > 11 or self.statBlock[2] > 11 or \
               self.statBlock[3] > 11 or self.statBlock[4] > 11 or self.statBlock[5] > 11:
                valid = True

    def create_widgets(self):
        #Table Headings
        self.attLbl = tk.Label(self, text = "Attribute")
        self.abrLbl = tk.Label(self, text="Abbreviation")
        self.scoreLbl = tk.Label(self, text="Score")
        self.attLbl.grid(row=1, column=0)
        self.abrLbl.grid(row=1, column=1)
        self.scoreLbl.grid(row=1, column=2)

        #Strength
        hdSTR = tk.Label(self, width = 40, height = 6, text = "Strength",
                         foreground = "red")
        self.strLbl = tk.Label(self, text="(STR)", foreground="red",
                               width=20)
        self.hdStrNum = tk.Label(self, text = str(self.statBlock[0]),
                            foreground = "red")
        hdSTR.grid(row = 2, column = 0)
        self.strLbl.grid(row = 2, column=1)
        self.hdStrNum.grid(row = 2, column = 2)

        #Dexterity
        hdDEX = tk.Label(self, width = 40, height = 6, text = "Dexterity",
                         foreground = "orange")
        self.dexLbl = tk.Label(self, text="(DEX)", foreground="orange",
                               width=20)
        self.hdDexNum = tk.Label(self, text = str(self.statBlock[1]),
                            foreground = "orange")
        self.hdDexNum.grid(row = 3, column = 2)
        self.dexLbl.grid(row = 3, column=1)
        hdDEX.grid(row = 3, column = 0)

        #Constitution
        hdCON = tk.Label(self, width = 40, height = 6, text = "Constitution",
                         foreground = "yellow")
        self.conLbl = tk.Label(self, text="(CON)", foreground="yellow",
                               width=20)
        self.hdConNum = tk.Label(self, text = str(self.statBlock[2]),
                            foreground = "yellow")
        hdCON.grid(row = 4, column = 0)
        self.conLbl.grid(row = 4, column=1)
        self.hdConNum.grid(row = 4, column = 2)
        #Intelligence        
        hdINT = tk.Label(self, width = 40, height = 6, text = "Intelligence",
                         foreground = "green")
        self.intLbl = tk.Label(self, text="(INT)", foreground="green",
                               width=20)
        self.hdIntNum = tk.Label(self, text = str(self.statBlock[3]),
                            foreground = "green")
        hdINT.grid(row = 5, column = 0)
        self.intLbl.grid(row = 5, column=1)
        self.hdIntNum.grid(row = 5, column = 2)
        
        #Wisdom
        hdWIS = tk.Label(self, width = 40, height = 6, text = "Wisdom",
                         foreground = "blue")
        self.wisLbl = tk.Label(self, text="(WIS)", foreground="blue",
                               width=20)
        self.hdWisNum = tk.Label(self, text = str(self.statBlock[4]),
                            foreground = "blue")
        hdWIS.grid(row = 6, column = 0)
        self.wisLbl.grid(row = 6, column=1)
        self.hdWisNum.grid(row = 6, column = 2)
        
        #Charisma
        hdCHA = tk.Label(self, width = 40, height = 6, text = "Charisma",
                         foreground = "indigo")
        self.chaLbl = tk.Label(self, text="(CHA)", foreground="indigo",
                               width=20)
        self.hdChaNum = tk.Label(self, text = str(self.statBlock[5]),
                            foreground = "indigo")
        hdCHA.grid(row = 7, column = 0)
        self.chaLbl.grid(row = 7, column=1)
        self.hdChaNum.grid(row = 7, column = 2)
        

        self.rrBttn = tk.Button(self, text = "Reroll", width=20,
                               command = self.re_roll)
        self.rrBttn.grid(row = 9, column = 0)

        self.backbutton = tk.Button(self, text="Back to Menu", width=20,
                           command=lambda: self.controller.show_frame("Menu"))
        self.backbutton.grid(row = 9, column = 1)

        self.saveBttn = tk.Button(self, text="Save and\nContinue", width=20,
                                  command=self.save_character)
        self.saveBttn.grid(row = 9, column = 2)

    def save_character(self):
        self.controller.player.strength = int(self.hdStrNum["text"])
        self.controller.player.dexterity = int(self. hdDexNum["text"])
        self.controller.player.constitution = int(self.hdConNum["text"])
        self.controller.player.intelligence = int(self.hdIntNum["text"])
        self.controller.player.wisdom = int(self.hdWisNum["text"])
        self.controller.player.charisma = int(self.hdChaNum["text"])
        print(self.controller.player)
        self.controller.show_frame("Menu")


    def re_roll(self):
        ''' re-roll the stat block '''
        self.roll_dice()

        self.hdStrNum["text"] = str(self.statBlock[0])
        self.hdDexNum["text"] = str(self.statBlock[1])
        self.hdConNum["text"] = str(self.statBlock[2])
        self.hdIntNum["text"] = str(self.statBlock[3])
        self.hdWisNum["text"] = str(self.statBlock[4])
        self.hdChaNum["text"] = str(self.statBlock[5])
        

class Simple(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        label = tk.Label(self, text="Simple", font=TITLE_FONT)
        label.grid(row = 0, column = 1)
        self.buttonClicks = 0
        self.create_widgets()

    def create_widgets(self):
        #Instructions
        if self.buttonClicks == 0:
            self.instructionLbl = tk.Label(self, text="Click a button to choose "+\
                                           "Most Important Attribute.",
                                           font = INSTRUCTION_FONT)
        self.instructionLbl.grid(row=1, column=0, columnspan = 4)
        
        #Table Headings
        self.attLbl = tk.Label(self, text = "Attribute")
        self.abrLbl = tk.Label(self, text="Abbreviation")
        self.scoreLbl = tk.Label(self, text="Score")
        self.attLbl.grid(row=2, column=0)
        self.abrLbl.grid(row=2, column=1)
        self.scoreLbl.grid(row=2, column=2)

        #Strength
        self.sSTR = tk.Button(self, width = 20, height = 2, text = "Strength",
                         foreground = "red", 
                         command=lambda:
                         self.bttnClick(1))
        self.strLbl = tk.Label(self, text="(STR)", foreground="red",
                               width=20)
        self.sStrNum = tk.Label(self, text = "12", foreground = "red")
        self.sSTR.grid(row = 3, column = 0)
        self.strLbl.grid(row = 3, column=1)
        self.sStrNum.grid(row = 3, column = 2)

        #Dexterity
        self.sDEX = tk.Button(self, width = 20, height = 2, text = "Dexterity",
                         foreground = "orange", command=lambda:
                         self.bttnClick(2))
        self.dexLbl = tk.Label(self, text="(DEX)", foreground="orange",
                               width=20)
        self.sDexNum = tk.Label(self, text = "12",
                                foreground = "orange")
        self.sDexNum.grid(row = 4, column = 2)
        self.dexLbl.grid(row = 4, column=1)
        self.sDEX.grid(row = 4, column = 0)

        #Constitution
        self.sCON = tk.Button(self, width = 20, height = 2, text = "Constitution",
                         foreground = "yellow", command=lambda:
                         self.bttnClick(3))
        self.conLbl = tk.Label(self, text="(CON)", foreground="yellow",
                               width=20)
        self.sConNum = tk.Label(self, text = "12",
                                foreground = "yellow")
        self.sCON.grid(row = 5, column = 0)
        self.conLbl.grid(row = 5, column=1)
        self.sConNum.grid(row = 5, column = 2)
        #Intelligence        
        self.sINT = tk.Button(self, width = 20, height = 2, text = "Intelligence",
                         foreground = "green", command=lambda:
                         self.bttnClick(4))
        self.intLbl = tk.Label(self, text="(INT)", foreground="green",
                               width=20)
        self.sIntNum = tk.Label(self, text = "12",
                                foreground = "green")
        self.sINT.grid(row = 6, column = 0)
        self.intLbl.grid(row = 6, column=1)
        self.sIntNum.grid(row = 6, column = 2)
        
        #Wisdom
        self.sWIS = tk.Button(self, width = 20, height = 2, text = "Wisdom",
                         foreground = "blue", command=lambda:
                         self.bttnClick(5))
        self.wisLbl = tk.Label(self, text="(WIS)", foreground="blue",
                               width=20)
        self.sWisNum = tk.Label(self, text = "12",
                                foreground = "blue")
        self.sWIS.grid(row = 7, column = 0)
        self.wisLbl.grid(row = 7, column=1)
        self.sWisNum.grid(row = 7, column = 2)
        
        #Charisma
        self.sCHA = tk.Button(self, width = 20, height = 2, text = "Charisma",
                         foreground = "indigo", command=lambda:
                         self.bttnClick(6))
        self.chaLbl = tk.Label(self, text="(CHA)", foreground="indigo",
                               width=20)
        self.sChaNum = tk.Label(self, text = "12",
                                foreground = "indigo")
        self.sCHA.grid(row = 8, column = 0)
        self.chaLbl.grid(row = 8, column=1)
        self.sChaNum.grid(row = 8, column = 2)


        #Bottom Row
        self.resetBttn = tk.Button(self, text = "Reset", width = 20,
                               command = lambda: self.reset())
        self.resetBttn.grid()

        self.backbutton = tk.Button(self, text="Back to Menu", width = 20,
                           command = lambda: self.controller.show_frame("Menu"))
        self.backbutton.grid(row = 9, column = 1)

        self.saveBttn = tk.Button(self, text="Save and\nContinue", width = 20,
                                  command = self.save_character, state = tk.DISABLED)
        self.saveBttn.grid(row = 9, column = 2)
        
    def save_character(self):
        self.controller.player.strength = int(self.sStrNum["text"])
        self.controller.player.dexterity = int(self. sDexNum["text"])
        self.controller.player.constitution = int(self.sConNum["text"])
        self.controller.player.intelligence = int(self.sIntNum["text"])
        self.controller.player.wisdom = int(self.sWisNum["text"])
        self.controller.player.charisma = int(self.sChaNum["text"])
        print(self.controller.player)
        self.controller.show_frame("Menu")

    def bttnClick(self, value):

        self.labelList = (self.sStrNum, self.sDexNum, self.sConNum,
                          self.sIntNum, self.sWisNum, self.sChaNum)
        buttonList = (self.sSTR, self.sDEX, self.sCON,
                      self.sINT, self.sWIS, self.sCHA)

        if self.buttonClicks == 0:
            self.labelList[value - 1].configure(text = "17")
        elif self.buttonClicks == 1:
            self.labelList[value - 1].configure(text = "9")
        buttonList[value-1].configure(state = tk.DISABLED)
        self.buttonClicks += 1
        self.update_instructions()
        if self.buttonClicks > 1:
            self.saveBttn["state"] = tk.NORMAL
            self.sSTR["state"] = tk.DISABLED
            self.sDEX["state"] = tk.DISABLED
            self.sCON["state"] = tk.DISABLED
            self.sINT["state"] = tk.DISABLED
            self.sWIS["state"] = tk.DISABLED
            self.sCHA["state"] = tk.DISABLED


    def update_instructions(self):
        '''change instructions as user picks their more favored Stats'''
        wordList = ("Most Important", "Least Important")
        word = ""
        if self.buttonClicks == 0:
            word = wordList[self.buttonClicks]
        elif self.buttonClicks == 1:
            word = wordList[self.buttonClicks]
        message = "Click a button to choose your " + word + " Attribute."
        self.instructionLbl["text"] = message

    def reset(self):
        '''enable all buttons, set labels back to blank'''
        self.buttonClicks = 0
        self.update_instructions()
        buttonList = (self.sSTR, self.sDEX, self.sCON,
                      self.sINT, self.sWIS, self.sCHA)
        for i in range(len(buttonList)):
            buttonList[i].configure(state = tk.NORMAL)

        self.sStrNum["text"] = "12"
        self.sDexNum["text"] = "12"
        self.sConNum["text"] = "12"
        self.sIntNum["text"] = "12"
        self.sWisNum["text"] = "12"
        self.sChaNum["text"] = "12"

class FourD6(tk.Frame):

    def __init__(self, parent, controller):
        '''class constructor'''
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.buttonClicks = 0
        self.statBlock = []
        for i in range(6):
            self.statBlock.append(self.roll_dice())

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.create_widgets()

    def roll_dice(self):
        '''roll 4d6, keep the highest'''

        rolls = []
        for i in range(4):
            rolls.append(rd.randint(1,6))
        rolls.remove(min(rolls))
        return sum(rolls)

    def create_widgets(self):
        '''method for widget placement'''
        #row 0 - Heading
        self.label = tk.Label(self, text="4 d 6", font=TITLE_FONT)
        self.label.grid(row=0, column=0, columnspan=3)

        #table headings
        self.attLbl = tk.Label(self, text="Attribute")
        self.abrLbl = tk.Label(self, text="Abbreviation")
        self.scoreLbl = tk.Label(self, text="Score")
        self.attLbl.grid(row=1, column=0)
        self.abrLbl.grid(row=1, column=1)
        self.scoreLbl.grid(row=1, column=2)

        #Strength
        self.strengthLbl = tk.Label(self, text="Strength", foreground="red",
                                    width=20)
        self.strLbl = tk.Label(self, text="(STR)", foreground="red",
                               width=20)
        self.strStatLbl = tk.Label(self, text="", foreground="red",
                                   width=20)
        self.strengthLbl.grid(row = 2, column=0)
        self.strLbl.grid(row = 2, column=1)
        self.strStatLbl.grid(row = 2, column=2)

        #Dexterity
        self.dexterityLbl = tk.Label(self, text="Dexterity", foreground="orange",
                                    width=20)
        self.dexLbl = tk.Label(self, text="(DEX)", foreground="orange",
                               width=20)
        self.dexStatLbl = tk.Label(self, text="", foreground="orange",
                                   width=20)
        self.dexterityLbl.grid(row = 3, column=0)
        self.dexLbl.grid(row = 3, column=1)
        self.dexStatLbl.grid(row = 3, column=2)

        #Constitution
        self.constitutionLbl = tk.Label(self, text="Constitution",
                                        foreground="yellow", width=20)
        self.conLbl = tk.Label(self, text="(CON)", foreground="yellow",
                               width=20)
        self.conStatLbl = tk.Label(self, text="", foreground="yellow",
                                   width=20)
        self.constitutionLbl.grid(row = 4, column=0)
        self.conLbl.grid(row = 4, column=1)
        self.conStatLbl.grid(row = 4, column=2)

        #Intelligence
        self.intelligenceLbl = tk.Label(self, text="Intelligence",
                                        foreground="green", width=20)
        self.intLbl = tk.Label(self, text="(INT)", foreground="green",
                               width=20)
        self.intStatLbl = tk.Label(self, text="", foreground="green",
                                   width=20)
        self.intelligenceLbl.grid(row = 5, column=0)
        self.intLbl.grid(row = 5, column=1)
        self.intStatLbl.grid(row = 5, column=2)

        #Wisdom
        self.wisdomLbl = tk.Label(self, text="Wisdom", foreground="blue",
                                  width=20)
        self.wisLbl = tk.Label(self, text="(WIS)", foreground="blue",
                               width=20)
        self.wisStatLbl = tk.Label(self, text="", foreground="blue",
                                   width=20)
        self.wisdomLbl.grid(row = 6, column=0)
        self.wisLbl.grid(row = 6, column=1)
        self.wisStatLbl.grid(row = 6, column=2)

        #Charisma
        self.charismaLbl = tk.Label(self, text="Charisma", foreground="indigo",
                                    width=20)
        self.chaLbl = tk.Label(self, text="(CHA)", foreground="indigo",
                               width=20)
        self.chaStatLbl = tk.Label(self, text="", foreground="indigo",
                                   width=20)
        self.charismaLbl.grid(row = 7, column=0)
        self.chaLbl.grid(row = 7, column=1)
        self.chaStatLbl.grid(row = 7, column=2)

        #subheading "Available scores"
        self.subHeadLbl = tk.Label(self, text="Available Scores",
                                   font = HEADING1_FONT)
        self.subHeadLbl.grid(row=8, column=0, columnspan=3)

        #Instructions
        self.instructionLbl = tk.Label(self, text="Click a button to choose "+\
                                       "your Strength score",
                                       font = INSTRUCTION_FONT)
        self.instructionLbl.grid(row=9, column=0, columnspan=3)

        #First row of score buttons
        self.bttn1 = tk.Button(self, text = str(self.statBlock[0]), width=20,
                               command=lambda:
                               self.bttnClick(1, str(self.statBlock[0])))
        self.bttn1.grid(row=10, column=0)

        self.bttn2 = tk.Button(self, text = str(self.statBlock[1]), width=20,
                               command=lambda:
                               self.bttnClick(2, str(self.statBlock[1])))
        self.bttn2.grid(row=10, column=1)

        self.bttn3 = tk.Button(self, text = str(self.statBlock[2]), width=20,
                               command=lambda:
                               self.bttnClick(3, str(self.statBlock[2])))
        self.bttn3.grid(row=10, column=2)

        #Second row of score buttons
        self.bttn4 = tk.Button(self, text = str(self.statBlock[3]), width=20,
                               command=lambda:
                               self.bttnClick(4, str(self.statBlock[3])))
        self.bttn4.grid(row=11, column=0)

        self.bttn5 = tk.Button(self, text = str(self.statBlock[4]), width=20,
                               command=lambda:
                               self.bttnClick(5, str(self.statBlock[4])))
        self.bttn5.grid(row=11, column=1)
                               
        self.bttn6 = tk.Button(self, text = str(self.statBlock[5]), width=20,
                               command=lambda:
                               self.bttnClick(6, str(self.statBlock[5])))
        self.bttn6.grid(row=11, column=2)

        #Reset button
        self.resetBttn = tk.Button(self, text = "Reset", width=20,
                               command = self.reset)
        self.resetBttn.grid(row=12, column=1)
        
        #Navigation Buttons
        self.rrBttn = tk.Button(self, text = "Reroll", width=20,
                               command = self.re_roll)
        self.rrBttn.grid()

        self.backbutton = tk.Button(self, text="Back to Menu", width=20,
                           command=lambda: self.controller.show_frame("Menu"))
        self.backbutton.grid(row=13, column=1)

        self.saveBttn = tk.Button(self, text="Save and\nContinue", width=20,
                                  command=self.save_character, state=tk.DISABLED)
        self.saveBttn.grid(row=13, column=2)
        
    def save_character(self):
        self.controller.player.strength = int(self.strStatLbl["text"])
        self.controller.player.dexterity = int(self. dexStatLbl["text"])
        self.controller.player.constitution = int(self.conStatLbl["text"])
        self.controller.player.intelligence = int(self.intStatLbl["text"])
        self.controller.player.wisdom = int(self.wisStatLbl["text"])
        self.controller.player.charisma = int(self.chaStatLbl["text"])
        print(self.controller.player)
        self.controller.show_frame("Menu")

    def re_roll(self):
        ''' re-roll the stat block '''
        buttonList = (self.bttn1, self.bttn2, self.bttn3,
                      self.bttn4, self.bttn5, self.bttn6)
        for i in range(len(self.statBlock)):
            self.statBlock[i] = rd.randint(3,18)
            buttonList[i].configure(text = str(self.statBlock[i]))
        self.reset()

    def reset(self):
        '''enable all buttons, set labels back to blank'''
        self.buttonClicks = 0
        self.update_instructions()
        buttonList = (self.bttn1, self.bttn2, self.bttn3,
                      self.bttn4, self.bttn5, self.bttn6)
        for i in range(len(buttonList)):
            buttonList[i].configure(state = tk.NORMAL)

        self.strStatLbl["text"] = ""
        self.dexStatLbl["text"] = ""
        self.conStatLbl["text"] = ""
        self.intStatLbl["text"] = ""
        self.wisStatLbl["text"] = ""
        self.chaStatLbl["text"] = ""
            
    def bttnClick(self, value, newText):

        self.labelList = (self.strStatLbl, self.dexStatLbl, self.conStatLbl,
                          self.intStatLbl, self.wisStatLbl, self.chaStatLbl)
        buttonList = (self.bttn1, self.bttn2, self.bttn3,
                      self.bttn4, self.bttn5, self.bttn6)

        self.labelList[self.buttonClicks].configure(text = newText)
        buttonList[value-1].configure(state = tk.DISABLED)
        self.buttonClicks += 1
        self.update_instructions()
        if self.buttonClicks > 5:
            self.saveBttn["state"] = tk.NORMAL

    def update_instructions(self):
        '''change instructions as user picks stats'''
        wordList = ("Strength", "Dexterity", "Constitution",
                    "Intelligence", "Wisdom", "Charisma")
        if self.buttonClicks < 6:
            word = wordList[self.buttonClicks]

            message = "Click a button to choose your " + word + " score."
            self.instructionLbl["text"] = message

             
class Help(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        label = tk.Label(self, text="Method Description", font=TITLE_FONT)
        label.grid(row = 0, column = 0, columnspan = 3)
        self.create_widgets()
        
    def create_widgets(self):     
        simpleLbl = tk.Label(self, text = "Simple", font=HEADING1_FONT)
        simpleLbl.grid(row = 1, column = 1)
        simpleTxt = tk.Text(self, width = 40, height = 6, wrap = 'word')
        simpleTxt.insert(0.0, SIMPLE_MESSAGE)
        simpleTxt.grid(row = 2, column = 0, columnspan = 3)
        simpleTxt.configure(state="disabled")

        hardLbl = tk.Label(self, text = "Hardcore", font=HEADING1_FONT)
        hardLbl.grid(row = 3, column = 1)
        hardcoreTxt = tk.Text(self, width = 40, height = 6, wrap = 'word')
        hardcoreTxt.insert(0.0, HARDCORE_MESSAGE)
        hardcoreTxt.grid(row = 4, column = 0, columnspan = 3)
        hardcoreTxt.configure(state="disabled")

        fourDLbl = tk.Label(self, text = "Four D6", font=HEADING1_FONT)
        fourDLbl.grid(row = 5, column = 1)
        fourDTxt = tk.Text(self, width = 40, height = 6, wrap = 'word')
        fourDTxt.insert(0.0, FOURD6_MESSAGE)
        fourDTxt.grid(row = 6, column = 0, columnspan = 3)
        fourDTxt.configure(state="disabled")
        
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: self.controller.show_frame("Menu"))
        button.grid(column = 1)



# main
root = RootApp()
root.title("Character Creator")
root.geometry("800x800")

root.mainloop()
