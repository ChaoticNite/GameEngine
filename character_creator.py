# character_creator.py
# Thorin Schmidt
# Edited by Noel Kling
# 11/29/2016

''' GUI-based character generator'''
import tkinter as tk
from character import *
from monster import *

TITLE_FONT = ("ms serif", 18, "bold")
HEADING_FONT = ("symbol", 14, "bold")
TEXT_FONT = ("comic sans", 9)
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

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        container = tk.Frame(self) 
        container.grid()
        container.grid_rowconfigure(8, weight=1)
        container.grid_columnconfigure(4, weight=1)

        self.frames = {}
        for F in (Menu, Hardcore, Simple, FourD6, Help):
            page_name = F.__name__
            frame = F(parent=container, controller=self) 
            self.frames[page_name] = frame  

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=8, column=4, sticky=(tk.N, tk.S, tk.E, tk.W))

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
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        # create instruction label
        self.instLbl = tk.Label(self, text =
                              "Choose a Character Creation Method:")
        self.instLbl.grid()

        # create whitespace
        self.blankLbl = tk.Label(self, text ="")
        self.blankLbl.grid()
        
        # create hardcore button
        self.hcBttn = tk.Button(self, text = "Hardcore",
                                command = lambda: self.controller.show_frame("Hardcore"))
        self.hcBttn.grid()

        # create simple button
        self.simpleBttn = tk.Button(self, text = "Simple",
                             command = lambda: self.controller.show_frame("Simple"))
        self.simpleBttn.grid()

        # create 4d6 button
        self.fourD6Bttn = tk.Button(self, text = "4d6",
                             command = lambda: self.controller.show_frame("FourD6"))
        self.fourD6Bttn.grid()

        # create a help button
        self.helpBttn = tk.Button(self, text = "Method Description",
                             command = lambda: self.controller.show_frame("Help"))
        self.helpBttn.grid()

class Hardcore(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hardcore", font=TITLE_FONT)
        label.grid(row = 1, column = 2, columnspan = 2)
        self.create_widgets()        
    def create_widgets(self):
        hdSTR = tk.Text(self, width = 40, height = 6, wrap = 'word', font = TEXT_FONT)
        hdSTR.insert(0.0, "Strength (STR)")
        hdSTR.grid(column = 1, columnspan = 2)
        hdDEX = tk.Text(self, width = 40, height = 6, wrap = 'word', font = TEXT_FONT)
        hdDEX.insert(0.0, "Dexterity (DEX)")
        hdDEX.grid(column = 1, columnspan = 2)
        hdCON = tk.Text(self, width = 40, height = 6, wrap = 'word', font = TEXT_FONT)
        hdCON.insert(0.0, "Constitution (CON)")
        hdCON.grid(column = 1, columnspan = 2)

        
        backButton = tk.Button(self, text="Back to Menu",
                           command=lambda: self.controller.show_frame("Menu"))
        backButton.grid(row = 8, column = 2, columnspan = 2)

class Simple(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Simple", font=TITLE_FONT)
        label.grid(row = 1, column = 2, columnspan = 2)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.grid()

class FourD6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="4 d 6", font=TITLE_FONT)
        label.grid(row = 1, column = 1, columnspan = 2)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.grid()

class Help(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):     
        label = tk.Label(self, text="Method Description", font=TITLE_FONT)
        label.grid()

        simpleLbl = tk.Label(self, text = "Simple", font=HEADING_FONT)
        simpleLbl.grid()
        simpleTxt = tk.Text(self, width = 40, height = 6, wrap = 'word', font = TEXT_FONT)
        simpleTxt.insert(0.0, SIMPLE_MESSAGE)
        simpleTxt.grid()
        simpleTxt.configure(state="disabled")

        hardLbl = tk.Label(self, text = "Hardcore", font=HEADING_FONT)
        hardLbl.grid()
        hardcoreTxt = tk.Text(self, width = 40, height = 6, wrap = 'word', font = TEXT_FONT)
        hardcoreTxt.insert(0.0, HARDCORE_MESSAGE)
        hardcoreTxt.grid()
        hardcoreTxt.configure(state="disabled")

        fourDLbl = tk.Label(self, text = "Four D6", font=HEADING_FONT)
        fourDLbl.grid()
        fourDTxt = tk.Text(self, width = 40, height = 6, wrap = 'word', font = TEXT_FONT)
        fourDTxt.insert(0.0, FOURD6_MESSAGE)
        fourDTxt.grid()
        fourDTxt.configure(state="disabled")
        
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: self.controller.show_frame("Menu"))
        button.grid()



# main
root = RootApp()
root.title("Character Creator")
root.geometry("400x400")

root.mainloop()
