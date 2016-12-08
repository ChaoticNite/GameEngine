# combat.py
# Noel Kling
# 12/07/2016

''' GUI-based Combat system '''
import tkinter as tk
import character as ch
from monster import *
from GameEngine import *

class Combat(tk.Frame):
    
    def __init__(self):
        tk.Frame.__init__(self)

        #Creates a monster and player.
        self.player = ch.Character()
        self.enemy = Orc()
        self.frame = tk.Frame(self, relief = "sunken", width = 1024, height = 1024)
        self.frame.grid(column = 0, row = 0, columnspan = 4, rowspan = 5)

        
        self.create_widgets()
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        #self.rowconfigure(0, weight = 1)
        #self.rowconfigure(1, weight = 1)
        #self.rowconfigure(2, weight = 1)
        #self.rowconfigure(3, weight = 1)
        #self.rowconfigure(4, weight = 1)
        #self.rowconfigure(5, weight = 3)

    def create_widgets(self):
        #Row-0
        self.heroImage = tk.PhotoImage(file = self.player.imageFileName)
        self.heroLbl = tk.Label(image = self.heroImage)
        self.attkImage = tk.PhotoImage(file = "attack.gif")
        self.attkBttn = tk.Button(self, text = "Attack", image = self.attkImage, compound = "left")
        self.enemyImage = tk.PhotoImage(file = self.enemy.imageFileName)
        self.enemyLbl = tk.Label(image = self.enemyImage)
        self.attkBttn.grid(row = 0, column = 1, sticky = (tk.E + tk.W))
        self.heroLbl.grid(row = 0, column = 0, sticky = tk.W)
        self.enemyLbl.grid(row = 0, column = 2, sticky = tk.E)

        #Row-1
        self.healImage = tk.PhotoImage(file = "heal.gif")
        self.healBttn = tk.Button(self, text = "Heal", image = self.healImage, compound = "left" )
        self.healBttn.grid(row = 1, column = 1, sticky = (tk.E + tk.W))
        
        #Row-2
        self.talkImage = tk.PhotoImage(file = "talk.gif")
        self.talkBttn = tk.Button(self, text = "Talk", image = self.talkImage, compound = "left")
        self.talkBttn.grid(row = 2, column = 1, sticky = (tk.E + tk.W))

        #Row-3
        self.runImage = tk.PhotoImage(file = "run.gif")
        self.runBttn = tk.Button(self, text = "Run", image = self.runImage, compound = "left")
        self.runBttn.grid(row = 3, column = 1, sticky = (tk.E + tk.W))

        #Row-4
        self.heroHealthLbl = tk.Label(text = str(self.player.health) + "/" + str(self.player.maxHealth))
        self.invBttn = tk.Button(self, text = "Inventory")
        self.enemyHealthLbl = tk.Label(text = str(self.enemy.health) + "/" + str(self.enemy.maxHealth))


        


root = tk.Tk()

app = Combat()
app.grid()

        

    
