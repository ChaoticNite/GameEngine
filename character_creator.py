# character_creator.py
# Thorin Schmidt
# Edited by Noel Kling
# 11/29/2016

''' GUI-based character generator'''
import tkinter as tk
from character import *
from monster import *
import random as rnd
from GameEngine import create_player

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
        self.statBlock = [rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18)]
        self.strVar = tk.StringVar()
        self.strVar = self.statBlock[0]
        self.create_widgets()        

    def create_widgets(self):
        hdSTR = tk.Label(self, width = 40, height = 6, text = "Strength (STR)",
                         font = TEXT_FONT, foreground = "red")
        hdSTR.grid(row = 1, column = 0, columnspan = 2)
        hdDEX = tk.Label(self, width = 40, height = 6, text = "Dexterity (DEX)",
                         font = TEXT_FONT, foreground = "orange")
        hdDEX.grid(row = 2, column = 0, columnspan = 2)
        hdCON = tk.Label(self, width = 40, height = 6, text = "Constitution (CON)",
                         font = TEXT_FONT, foreground = "yellow")
        hdCON.grid(row = 3, column = 0, columnspan = 2)
        hdINT = tk.Label(self, width = 40, height = 6, text = "Intelligence (INT)",
                         font = TEXT_FONT, foreground = "green")
        hdINT.grid(row = 4, column = 0, columnspan = 2)
        hdWIS = tk.Label(self, width = 40, height = 6, text = "Wisdom (WIS)",
                         font = TEXT_FONT, foreground = "blue")
        hdWIS.grid(row = 5, column = 0, columnspan = 2)
        hdCHA = tk.Label(self, width = 40, height = 6, text = "Charisma (CHA)",
                         font = TEXT_FONT, foreground = "indigo")
        hdCHA.grid(row = 6, column = 0, columnspan = 2)

        hdStrNum = tk.Label(self, text = str(self.statBlock[0]), font = TEXT_FONT,
                            foreground = "red")
        hdStrNum.grid(row = 2, column = 1)
        hdDexNum = tk.Label(self, text = str(self.statBlock[1]), font = TEXT_FONT,
                            foreground = "orange")
        hdDexNum.grid(row = 3, column = 1)

        
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
        label.grid(row = 0, column = 1, columnspan = 2)
        self.statBlock = [rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18),
                          rnd.randint(3,18)]
        self.counter = 0
        self.strVar = tk.StringVar()
        self.strVar = self.statBlock[0]
        self.create_widgets()
                
        
    def create_widgets(self):
        dSTR = tk.Label(self, width = 40, height = 6, text = "Strength (STR)",
                         font = TEXT_FONT, foreground = "red")
        dSTR.grid(row = 1, column = 0, columnspan = 2)
        dDEX = tk.Label(self, width = 40, height = 6, text = "Dexterity (DEX)",
                         font = TEXT_FONT, foreground = "orange")
        dDEX.grid(row = 2, column = 0, columnspan = 2)
        dCON = tk.Label(self, width = 40, height = 6, text = "Constitution (CON)",
                         font = TEXT_FONT, foreground = "yellow")
        dCON.grid(row = 3, column = 0, columnspan = 2)
        dINT = tk.Label(self, width = 40, height = 6, text = "Intelligence (INT)",
                         font = TEXT_FONT, foreground = "green")
        dINT.grid(row = 4, column = 0, columnspan = 2)
        dWIS = tk.Label(self, width = 40, height = 6, text = "Wisdom (WIS)",
                         font = TEXT_FONT, foreground = "blue")
        dWIS.grid(row = 5, column = 0, columnspan = 2)
        dCHA = tk.Label(self, width = 40, height = 6, text = "Charisma (CHA)",
                         font = TEXT_FONT, foreground = "indigo")
        dCHA.grid(row = 6, column = 0, columnspan = 2)

        dSBox = tk.Entry(self)
        dSBox.grid(row = 1, column = 2)
        dDBox = tk.Entry(self)
        dDBox.grid(row = 2, column = 2)
        dCONBox = tk.Entry(self)
        dCONBox.grid(row = 3, column = 2)
        dIBox = tk.Entry(self)
        dIBox.grid(row = 4, column = 2)
        dWBox = tk.Entry(self)
        dWBox.grid(row = 5, column = 2)
        dCBox = tk.Entry(self)
        dCBox.grid(row = 6, column = 2)

        opNum1 = tk.Button(self, text = str(self.statBlock[0]))
        opNum2 = tk.Button(self, text = str(self.statBlock[1]))
        opNum3 = tk.Button(self, text = str(self.statBlock[2]))
        opNum4 = tk.Button(self, text = str(self.statBlock[3]))
        opNum5 = tk.Button(self, text = str(self.statBlock[4]))
        opNum6 = tk.Button(self, text = str(self.statBlock[5]))

        #self.buttons_rule()        
        #self.killme()
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: self.controller.show_frame("Menu"))
        button.grid()

    def buttons_rule():
        valid = False
        #while not valid:
            #opNum1.configure(command = lambda statBlock[1]=statBlock[1]: 
            
        
        
    def killme(self):        
        if self.counter == 0:
            dSBox.configure(state = 'normal')
            dDBox.configure(state = 'disabled')
            dCONBox.configure(state = 'disabled')
            dIBox.configure(state = 'disabled')
            dWBox.configure(state = 'disabled')
            dCBox/configure(state = 'disabled')

        elif self.counter == 1:
            dSBox.configure(state = 'disabled')
            dDBox.configure(state = 'normal')
            dCONBox.configure(state = 'disabled')
            dIBox.configure(state = 'disabled')
            dWBox.configure(state = 'disabled')
            dCBox.configure(state = 'disabled')
    
        elif self.counter == 2:
            dSBox.configure(state = 'disabled')
            dDBox.configure(state = 'disabled')
            dCONBox.configure(state = 'normal')
            dIBox.configure(state = 'disabled')
            dWBox.configure(state = 'disabled')
            dCBox.configure(state = 'disabled')
    
        elif self.counter == 3:
            dSBox.configure(state = 'disabled')
            dDBox.configure(state = 'disabled')
            dCONBox.configure(state = 'disabled')
            dIBox.configure(state = 'normal')
            dWBox.configure(state = 'disabled')
            dCBox.configure(state = 'disabled')
            
        elif self.counter == 4:
            dSBox.configure(state = 'disabled')
            dDBox.configure(state = 'disabled')
            dCONBox.configure(state = 'disabled')
            dIBox.configure(state = 'disabled')
            dWBox.configure(state = 'normal')
            dCBox.configure(state = 'disabled')

        elif self.counter == 5:
            dSBox.configure(state = 'disabled')
            dDBox.configure(state = 'disabled')
            dCONBox.configure(state = 'disabled')
            dIBox.configure(state = 'disabled')
            dWBox.configure(state = 'disabled')
            dCBox.configure(state = 'normal')

        else:
            dSBox.configure(state = 'disabled')
            dDBox.configure(state = 'disabled')
            dCONBox.configure(state = 'disabled')
            dIBox.configure(state = 'disabled')
            dWBox.configure(state = 'disabled')
            dCBox.configure(state = 'disabled')
             
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
