# combat_gui.py
# Travis Kipp
# 11/29/2016

''' GUI-based combat system'''

import random as rd
import tkinter as tk
from GameEngine import *
import character as ch
from monster import *

TITLE_FONT = ("Helvetica", 20, "bold")
HEADING1_FONT = ("Helvetica", 16, "bold")
TABLE_FONT = ("Arial", 10, "bold")
INSTRUCTION_FONT = ("Helvetica", 14, "bold")
LOG_EXAMPLE = ("You are now in Combat.\nWhat are you going to do next?")

class RootApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in [CombatSystem, Inventory]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("CombatSystem")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class CombatSystem(tk.Frame):
    def __init__(self, parent, controller):
        """ Initialize the frame. """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=0)

    def create_widgets(self):
        '''Widgets are created here and grided'''

        #Option buttons
        optionLabel = tk.Label(self, text="Options")
        optionLabel.grid(row = 0, column = 1)
        attackButton = tk.Button(self, text='Attack',font=('MS', 8,'bold'))
        attackButton.grid(row = 1, column = 1, sticky= tk.E + tk.W)
        fleeButton = tk.Button(self, text='Flee',font=('MS', 8,'bold'))
        fleeButton.grid(row = 2, column = 1, sticky = tk.E + tk.W)
        healButton = tk.Button(self, text='Heal',font=('MS', 8,'bold'))
        healButton.grid(row = 3, column = 1, sticky = tk.E + tk.W)
        invButton = tk.Button(self, text = "Inventory", font=('MS', 8,'bold'),
                             command = lambda: self.controller.show_frame("Inventory"))
        invButton.grid(row = 4, column = 1, sticky = tk.E + tk.W)
        talkButton = tk.Button(self, text='Talk',font=('MS', 8,'bold'))
        talkButton.grid(row = 5, column = 1, sticky = tk.E + tk.W)
        talkButton.configure(state=tk.DISABLED)

        #Monster image and name
        enemyName = tk.Label(self, text ="Monster Name")
        enemyName.grid(row = 0, column = 2)
        enemy = tk.PhotoImage(file = 'Roy.gif')
        enemyLabel = tk.Label(self, image=enemy)
        enemyLabel.image = enemy
        enemyLabel.grid(row = 1, column = 2, rowspan = 5, sticky=tk.NSEW)

        #Player image and name
        you = tk.PhotoImage(file = 'Roy.gif')
        youName = tk.Label(self, text="Your Name")
        youName.grid(row = 0, column = 0)
        youLabel = tk.Label(self, image=you)
        youLabel.image = you
        youLabel.grid(row = 1, column = 0, rowspan = 5, sticky=tk.NSEW)

        #HP
        yourHpLabel = tk.Label(self, text = "HP")
        yourHpLabel.grid(row=5, column=0)

        enemyHpLabel = tk.Label(self, text = "HP")
        enemyHpLabel.grid(row=5, column=2)

        #row 1 - table headings
        self.attLbl = tk.Label(self, text="Stats")
        self.abrLbl = tk.Label(self, text="Log")
        self.scoreLbl = tk.Label(self, text="Stats")
        self.attLbl.grid(row=6, column=0)
        self.abrLbl.grid(row=6, column=1)
        self.scoreLbl.grid(row=6, column=2)

        #Enemy Stats
        #row 2 - Strength
        self.strLbl = tk.Label(self, text="(STR)", background="red",
                               font=TABLE_FONT, width=12)
        self.strStatLbl = tk.Label(self, text='Strength', background="red",
                                   font=TABLE_FONT, width=12)
        self.strLbl.grid(row = 7, column=2)
        self.strStatLbl.grid(row = 8, column=2)

        #row 3 - Dexterity
        self.dexLbl = tk.Label(self, text="(DEX)", background="orange",
                               font=TABLE_FONT, width=12)
        self.dexStatLbl = tk.Label(self, text='Dexterity', background="orange",
                                   font=TABLE_FONT, width=12)
        self.dexLbl.grid(row = 9, column=2)
        self.dexStatLbl.grid(row = 10, column=2)

        #row 4 - Constitution
        self.conLbl = tk.Label(self, text="(CON)", background="yellow",
                               font=TABLE_FONT, width=12)
        self.conStatLbl = tk.Label(self, text='Constitution', background="yellow",
                                   font=TABLE_FONT, width=12)
        self.conLbl.grid(row = 11, column=2)
        self.conStatLbl.grid(row = 12, column=2)

        #row 5 - Intelligence
        self.intLbl = tk.Label(self, text="(INT)", background="green",
                               font=TABLE_FONT, width=12)
        self.intStatLbl = tk.Label(self, text='Intellegence', background="green",
                                   font=TABLE_FONT, width=12)
        self.intLbl.grid(row = 13, column=2)
        self.intStatLbl.grid(row = 14, column=2)

        #row 6 - Wisdom
        self.wisLbl = tk.Label(self, text="(WIS)", background="cyan",
                               font=TABLE_FONT, width=12)
        self.wisStatLbl = tk.Label(self, text='Wisdom', background="cyan",
                                   font=TABLE_FONT, width=12)
        self.wisLbl.grid(row = 15, column=2)
        self.wisStatLbl.grid(row = 16, column=2)

        #row 7 - Charisma
        self.chaLbl = tk.Label(self, text="(CHA)", background="magenta3",
                               font=TABLE_FONT, width=12)
        self.chaStatLbl = tk.Label(self, text='Charisma', background="magenta3",
                                   font=TABLE_FONT, width=12)
        self.chaLbl.grid(row = 17, column=2)
        self.chaStatLbl.grid(row = 18, column=2)

        #Log text box
        logTxt = tk.Text(self, height = 6, wrap = "word")
        logTxt.insert(0.0, LOG_EXAMPLE)
        logTxt.grid(row = 7, column = 1, rowspan = 100)

        #Your Stats
        #row 2 - Strength
        self.strLbl = tk.Label(self, text="(STR)", background="red",
                               font=TABLE_FONT, width=12)
        self.strStatLbl = tk.Label(self, text='Strength', background="red",
                                   font=TABLE_FONT, width=12)
        self.strLbl.grid(row = 7, column=0)
        self.strStatLbl.grid(row = 8, column=0)

        #row 3 - Dexterity
        self.dexLbl = tk.Label(self, text="(DEX)", background="orange",
                               font=TABLE_FONT, width=12)
        self.dexStatLbl = tk.Label(self, text='Dexterity', background="orange",
                                   font=TABLE_FONT, width=12)
        self.dexLbl.grid(row = 9, column=0)
        self.dexStatLbl.grid(row = 10, column=0)

        #row 4 - Constitution
        self.conLbl = tk.Label(self, text="(CON)", background="yellow",
                               font=TABLE_FONT, width=12)
        self.conStatLbl = tk.Label(self, text='Constitution', background="yellow",
                                   font=TABLE_FONT, width=12)
        self.conLbl.grid(row = 11, column=0)
        self.conStatLbl.grid(row = 12, column=0)

        #row 5 - Intelligence
        self.intLbl = tk.Label(self, text="(INT)", background="green",
                               font=TABLE_FONT, width=12)
        self.intStatLbl = tk.Label(self, text='Intellegence', background="green",
                                   font=TABLE_FONT, width=12)
        self.intLbl.grid(row = 13, column=0)
        self.intStatLbl.grid(row = 14, column=0)

        #row 6 - Wisdom
        self.wisLbl = tk.Label(self, text="(WIS)", background="cyan",
                               font=TABLE_FONT, width=12)
        self.wisStatLbl = tk.Label(self, text='Wisdom', background="cyan",
                                   font=TABLE_FONT, width=12)
        self.wisLbl.grid(row = 15, column=0)
        self.wisStatLbl.grid(row = 16, column=0)

        #row 7 - Charisma
        self.chaLbl = tk.Label(self, text="(CHA)", background="magenta3",
                               font=TABLE_FONT, width=12)
        self.chaStatLbl = tk.Label(self, text='Charisma', background="magenta3",
                                   font=TABLE_FONT, width=12)
        self.chaLbl.grid(row = 17, column=0)
        self.chaStatLbl.grid(row = 18, column=0)

class Inventory(tk.Frame):
    def __init__(self, parent, controller):
        """ Initialize the frame. """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid()
        self.create_widgets()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        #self.rowconfigure(0, weight=int(0.1))
        #self.rowconfigure(1, weight=int(0.1))
        #self.rowconfigure(2, weight=int(0.1))
        #self.rowconfigure(3, weight=int(0.1))

    def create_widgets(self):
        you = tk.PhotoImage(file = "Roy.gif")

        #Close button
        self.closeBttn = tk.Button(self, text = "Close",
                             command = lambda: self.controller.show_frame("CombatSystem"))
        self.closeBttn.grid()

        potionsLbl = tk.Label(self, text = "Potions =")
        potionsLbl.grid(row = 1, column = 1)

        potionsNum = tk.Label(self, text = "#")
        potionsNum.grid(row = 1, column = 2)

root = RootApp()
root.title("You're in combat")
root.geometry("1024x1024+250+250")
root.mainloop()
