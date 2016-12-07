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

        self.player = ch.Character()
        ''' self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        self.rowconfigure(5, weight = 3)'''
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        #Row 0
        self.heroImage = tk.PhotoImage(file = self.player.imageFileName)
        self.heroLbl = tk.Label(image = self.heroImage)
        self.attkImage = tk.PhotoImage(file = "attack.gif")
        self.attkLbl = tk.Label(image = self.attkImage)
        self.attkBttn = tk.Button(self, text = "Attack")
        #self.heroLbl.grid(row = 0, column = 0, rowspan = 3)
        self.attkLbl.grid(row = 0, column = 1)
        self.attkBttn.grid(row = 0, column = 2)
        self.heroLbl.grid(row = 0, column = 0, rowspan = 3)


root = tk.Tk()

app = Combat()
app.grid()

        

        

    
