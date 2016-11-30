# character_creator.py
# Thorin Schmidt
# Edited by Noel Kling
# 11/29/2016

''' GUI-based character generator'''
import tkinter as tk
from character import *
from monster import *

TITLE_FONT = ("Helvetica", 18, "bold")
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
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Hardcore, Simple, FourD6, Help):
            page_name = F.__name__
            frame = F(parent=container, controller=self) 
            self.frames[page_name] = frame  

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

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
        self.instLbl.pack()

        # create whitespace
        self.blankLbl = tk.Label(self, text ="")
        self.blankLbl.pack()
        
        # create hardcore button
        self.hcBttn = tk.Button(self, text = "Hardcore",
                                command = lambda: self.controller.show_frame("Hardcore"))
        self.hcBttn.pack()

        # create simple button
        self.simpleBttn = tk.Button(self, text = "Simple",
                             command = lambda: self.controller.show_frame("Simple"))
        self.simpleBttn.pack()

        # create 4d6 button
        self.fourD6Bttn = tk.Button(self, text = "4d6",
                             command = lambda: self.controller.show_frame("FourD6"))
        self.fourD6Bttn.pack()

        # create a help button
        self.helpBttn = tk.Button(self, text = "Help",
                             command = lambda: self.controller.show_frame("Help"))
        self.helpBttn.pack()

class Hardcore(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Hardcore", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()

class Simple(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Simple", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()

class FourD6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="4 d 6", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()

class Help(tk.Frame):

    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
    def create_widgets(self):     
        label = tk.Label(self, text="Method Description", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        simpleLbl = tk.Label(self, text = "Simple")
        simpleLbl.pack()
        simpleTxt = tk.Text(self, width = 40, height = 6, wrap = 'word')
        simpleTxt.insert(0.0, SIMPLE_MESSAGE)
        simpleTxt.pack()

        hardLbl = tk.Label(self, text = "Hardcore")
        hardLbl.pack()
        hardcoreTxt = tk.Text(self, width = 40, height = 6, wrap = 'word')
        hardcoreTxt.insert(0.0, HARDCORE_MESSAGE)
        hardcoreTxt.pack()

        fourDLbl = tk.Label(self, text = "Four D6")
        fourDLbl.pack()
        fourDTxt = tk.Text(self, width = 40, height = 6, wrap = 'word')
        fourDTxt.insert(0.0, FOURD6_MESSAGE)
        fourDTxt.pack()
        
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: self.controller.show_frame("Menu"))
        button.pack()



# main
root = RootApp()
root.title("Character Creator")
root.geometry("400x400")

root.mainloop()
