class EXAMPLE(tk.Frame):

    def __init__(self, parent, controller):
        '''class constructor'''
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        
        '''STR, DEX, CON, INT, WIS, CHA'''
        self.statBlock = [rd.randint(3,18),
                          rd.randint(3,18),
                          rd.randint(3,18),
                          rd.randint(3,18),
                          rd.randint(3,18),
                          rd.randint(3,18)]

        self.create_widgets()

    def create_widgets(self):
        '''method for widget placement'''
        
        self.label = tk.Label(self, text="Hardcore", font=TITLE_FONT)
        self.label.grid(row=0, column=0, columnspan=3)

        self.bttn1 = tk.Button(self, text = str(self.statBlock[0]),
                               command=lambda:
                               self.bttnClick(str(self.statBlock[0])))
        self.bttn1.grid(row=1, column=0)

        self.bttn2 = tk.Button(self, text = str(self.statBlock[1]),
                               command=lambda:
                               self.bttnClick(str(self.statBlock[1])))
        self.bttn2.grid(row=1, column=1)

        self.bttn3 = tk.Button(self, text = str(self.statBlock[2]),
                               command=lambda:
                               self.bttnClick(str(self.statBlock[2])))
        self.bttn3.grid(row=1, column=2)

        self.bttn4 = tk.Button(self, text = str(self.statBlock[3]),
                               command=lambda:
                               self.bttnClick(str(self.statBlock[3])))
        self.bttn4.grid(row=2, column=0)

        self.bttn5 = tk.Button(self, text = str(self.statBlock[4]),
                               command=lambda:
                               self.bttnClick(str(self.statBlock[4])))
        self.bttn5.grid(row=2, column=1)
                               
        self.bttn6 = tk.Button(self, text = str(self.statBlock[5]),
                               command=lambda:
                               self.bttnClick(str(self.statBlock[5])))
        self.bttn6.grid(row=2, column=2)
                            


        self.label2 = tk.Label(self, text = "none")
        self.label2.grid()
     
        self.button = tk.Button(self, text="Back to Menu",
                           command=lambda: self.controller.show_frame("Menu"))
        self.button.grid()

    def re_roll(self):
        ''' re-roll the stat block '''
        for i in range(len(self.statBlock)):
            self.statBlock[i] = rd.randint(3,18)
            
    def bttnClick(self, newText):
        self.label2['text'] = newText

