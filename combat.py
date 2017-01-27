# combat.py
# Noel Kling
# 12/07/2016

''' GUI-based Combat system '''
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
        
class Combat(tk.Frame):
    
    def __init__(self,master):
        
        tk.Frame.__init__(self)

        #Creates a monster and player.
        self.player = ch.Character()
        self.enemy = Monster()
        self.frame = tk.Frame(self, relief = "sunken", width = 1024, height = 1024)
        self.frame.grid(column = 0, row = 0, columnspan = 4, rowspan = 5)

        self.grid()
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 1)
        self.create_widgets()
        

    def create_widgets(self):
        #Row-0
        self.opLabel = tk.Label(self, text = "Options")
        self.heroName = tk.Label(self, text = self.player.name)
        self.enemyName = tk.Label(self, text = self.enemy.name)
        self.opLabel.grid(row = 0, column = 1)
        self.heroName.grid(row = 0, column = 0)
        self.enemyName.grid(row = 0, column = 2)

        #Row-1
        self.heroImage = tk.PhotoImage(file = self.player.imageFileName)
        self.heroLbl = tk.Label(self, image = self.heroImage)
        self.heroLbl.image = self.heroImage
        self.attkImage = tk.PhotoImage(file = "attack.gif")
        self.attkBttn = tk.Button(self, height = 35, text = "Attack", image = self.attkImage, compound = "left")
        self.enemyImage = tk.PhotoImage(file = self.enemy.imageFileName)
        self.enemyLbl = tk.Label(self, image = self.enemyImage)
        self.enemyLbl.image = self.enemyImage
        self.attkBttn.grid(row = 1, column = 1, sticky = (tk.E + tk.W))
        #self.heroLbl.grid(row = 1, column = 0, rowspan = 5, sticky = (tk.W + tk.N))
        #self.enemyLbl.grid(row = 1, column = 2, rowspan = 5, sticky = (tk.E + tk.N))

        #Row-2
        self.healImage = tk.PhotoImage(file = "heal.gif")
        self.healBttn = tk.Button(self, height = 35, text = "Heal", image = self.healImage, compound = "left" )
        self.healBttn.grid(row = 2, column = 1, sticky = (tk.E + tk.W))
        
        #Row-3
        self.talkImage = tk.PhotoImage(file = "talk.gif")
        self.talkBttn = tk.Button(self, height = 35, text = "Talk", image = self.talkImage, compound = "left")
        self.talkBttn.grid(row = 3, column = 1, sticky = (tk.E + tk.W))

        #Row-4
        self.runImage = tk.PhotoImage(file = "run.gif")
        self.runBttn = tk.Button(self, height = 35, text = "Run", image = self.runImage, compound = "left")
        self.runBttn.grid(row = 4, column = 1, sticky = (tk.E + tk.W))

        #Row-5
        self.heroHealthLbl = tk.Label(text = str(self.player.health) + "/" + str(self.player.maxHealth),
                                      width = 20)
        self.invBttn = tk.Button(self, height = 5, text = "Inventory")
        self.enemyHealthLbl = tk.Label(text = str(self.enemy.health) + "/" + str(self.enemy.maxHealth),
                                       width = 20)
        self.heroHealthLbl.grid(row = 5, column = 0)
        self.invBttn.grid(row = 5, column = 1, sticky = (tk.E + tk.W + tk.N))
        self.enemyHealthLbl.grid(row = 5, column = 2)

        #Row-6
        self.logBox = tk.Text(self, width = 25)
        self.logBox.insert(0.0, self.player.strength)
        self.logBox.grid(row = 6, column = 0, sticky = tk.E)


#main    
root = tk.Tk()
root.title("Combat")
root.geometry("1024x1024+250+250")
app = Combat(root)
app.grid()

        

    
