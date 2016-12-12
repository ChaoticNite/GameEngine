# combat.py
# Noel Kling
# 12/07/2016

''' GUI-based Combat system '''
import tkinter as tk
import character as ch
from monster import *
from GameEngine import *

class Combat(tk.Frame):
    
    def __init__(self,master):
        
        tk.Frame.__init__(self)

        #Creates a monster and player.
        self.player = ch.Character()
        self.enemy = Orc()
        self.frame = tk.Frame(self, relief = "sunken", width = 1024, height = 1024)
        self.frame.grid(column = 0, row = 0, columnspan = 4, rowspan = 5)

        self.grid()
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.create_widgets()
        

    def create_widgets(self):

        #Row-0
        self.heroImage = tk.PhotoImage(file = self.player.imageFileName)
        self.heroLbl = tk.Label(image = self.heroImage, width = 200)
        self.attkImage = tk.PhotoImage(file = "attack.gif")
        self.attkBttn = tk.Button(self, height = 35, text = "Attack", image = self.attkImage, compound = "left")
        self.enemyImage = tk.PhotoImage(file = self.enemy.imageFileName)
        self.enemyLbl = tk.Label(image = self.enemyImage, width = 200)
        self.attkBttn.grid(row = 0, column = 1, sticky = (tk.E + tk.W))
        self.heroLbl.grid(row = 0, sticky = (tk.W + tk.N), rowspan = 2)
        self.enemyLbl.grid(row = 0, sticky = (tk.E + tk.N), rowspan = 2)

        #Row-1
        self.healImage = tk.PhotoImage(file = "heal.gif")
        self.healBttn = tk.Button(self, height = 35, text = "Heal", image = self.healImage, compound = "left" )
        self.healBttn.grid(row = 1, column = 1, sticky = (tk.E + tk.W))
        
        #Row-2
        self.talkImage = tk.PhotoImage(file = "talk.gif")
        self.talkBttn = tk.Button(self, height = 35, text = "Talk", image = self.talkImage, compound = "left")
        self.talkBttn.grid(row = 2, column = 1, sticky = (tk.E + tk.W))

        #Row-3
        self.runImage = tk.PhotoImage(file = "run.gif")
        self.runBttn = tk.Button(self, height = 35, text = "Run", image = self.runImage, compound = "left")
        self.runBttn.grid(row = 3, column = 1, sticky = (tk.E + tk.W))

        #Row-4
        self.heroHealthLbl = tk.Label(text = str(self.player.health) + "/" + str(self.player.maxHealth), width = 20)
        self.invBttn = tk.Button(self, height = 35, text = "Inventory")
        self.enemyHealthLbl = tk.Label(text = str(self.enemy.health) + "/" + str(self.enemy.maxHealth), width = 20)
        self.heroHealthLbl.grid(row = 4, column = 0, sticky = tk.W)
        self.invBttn.grid(row = 4, column = 1, sticky = (tk.E + tk.W))
        self.enemyHealthLbl.grid(row = 4, column = 2, sticky = (tk.E + tk.W))

        #Row-5
        #self.logBox = tk.Textbox(self, 

root = tk.Tk()
root.columnconfigure(1, weight = 1)
root.title("Combat")
app = Combat(root)
app.grid()

        

    
