#animals.png

import tkinter as tk
from tkinter import Frame
import random
import time
import main_menu

class Animals:
    
    def __init__(self, root):
        self.score=0 #Score counter
        self.root=root #Using root created in main_menu
        self.list_animals=["Tigers", "Zebras", "Lemurs", "Elephants", "Pandas"] #List of possible animals
        self.chosen_animal=self.list_animals[random.randint(0,4)] #Randomly chooses animal for user to count
        self.correct_ans=0 #Keeps track of how many of the chosen animal are created in order to know the correct answer
        
    def gameplay(self):
        ##Window##
        self.root.grid()
        self.root.title("Animals") #Name of the window
        ##Canvas##
        #Frame
        frame=Frame(self.root)
        frame.pack()
        self.canvas=tk.Canvas(frame, bg="white", width=800, height=500)
        self.canvas.pack()
        #Background/label
        bg_image=tk.PhotoImage(file="ANIMALSbackground.gif")
        self.canvas.create_image(0, 200, image=bg_image, anchor="w")
        
        ##Score Display##
        score_label=tk.Label(self.root, text=["Score:", self.score], font=("Courier", 20), fg="red", bg="white")
        score_label.pack()
        score_label.place(x=650, y=450)
        
        ##Popup Menu##
        popupmenu1=tk.Label(self.canvas, text=("Count all the"), font=("Courier", 12), anchor="n", bg="white", fg="black", height=7, width=20)
        popupmenu2=tk.Label(self.canvas, text=(self.chosen_animal), font=("Courier", 12), anchor="n", bg="white", fg="red", height=7)
        popupmenu1.place(x=330, y=180)
        popupmenu2.place(x=473, y=180)
        #Return to Menu Button
        returnmenu=tk.Button(self.canvas, text="Main Menu", bg="white", command=self.returntomenu)
        returnmenu.place(x=420, y=240)
        #Start Button
        start=tk.Button(self.canvas, text="Start", bg="white")
        start.config(command=lambda: self.RandomAnimals(popupmenu1, popupmenu2, start, returnmenu, tiger, zebra, lemur, elephant, panda, 20, score_label))
        start.place(x=350, y=240)
        
        ##Making Animals Into Images##
        #Tiger
        tiger_image=tk.PhotoImage(file="Tiger.gif")
        tiger=tiger_image.subsample(3, 3)
        
        #Zebra
        zebra_image=tk.PhotoImage(file="Zebra.gif")
        zebra=zebra_image.subsample(3, 3)
        
        #Lemur
        lemur_image=tk.PhotoImage(file="Lemur.gif")
        lemur=lemur_image.subsample(3, 3)
        
        #Elephant
        elephant_image=tk.PhotoImage(file="Elephant.gif")
        elephant=elephant_image.subsample(6, 6)
        
        #Panda
        panda_image=tk.PhotoImage(file="Panda.gif")
        panda=panda_image.subsample(5, 5)

        
        #Keep running
        self.root.mainloop()   
        
        
    def RandomAnimals(self, label1, label2, button1, button2, tiger, zebra, lemur, elephant, panda, count, score_label):
        #Removes popup menu and buttons
        label1.destroy()
        label2.destroy()
        button1.destroy()
        button2.destroy()
        
        ##Entry for Answer##
        #Label "total"
        total_label=tk.Label(self.root, text="Total:", bg="white")
        total_label.place(x=260, y=460)
        #Actual entry bar
        total_entry=tk.Entry(self.root)
        total_entry.place(x=305, y=459)
        #Submit answer button
        total_submit=tk.Button(self.root, text="Submit", bg="white", command=lambda: self.iscorrect(total_entry, score_label))
        total_submit.place(x=480, y=454)
        
        ##Recursive Gameplay##
        #This game prints 20 animals as indicated by the count parameter given by the start button
        #Once all 20 animals are printed, there is a return statement to stop the recursion
        if count==0:
            self.time=False
            return self.correct_ans
        
        #Otherwise, print 20 animals randomly
        else:
            which_animal=random.randint(1,5)
            #Tiger
            if which_animal==1:
                tiger1=self.canvas.create_image(random.randint(50,710), random.randint(100,410), image=tiger)
                if self.chosen_animal=="Tigers": #Keeps track of whether the program has printed a "chosen animal"
                    self.correct_ans=self.correct_ans+1 #Then it adds to correct answer
                
            #Zebra
            elif which_animal==2:
                zebra1=self.canvas.create_image(random.randint(50,710), random.randint(100,410), image=zebra)
                if self.chosen_animal=="Zebras":
                    self.correct_ans=self.correct_ans+1
                
            #Lemur
            elif which_animal==3:
                lemur1=self.canvas.create_image(random.randint(50,710), random.randint(100,410), image=lemur)
                if self.chosen_animal=="Lemurs":
                    self.correct_ans=self.correct_ans+1
               
            #Elephant
            elif which_animal==4:
                elephant1=self.canvas.create_image(random.randint(50,710), random.randint(100,410), image=elephant)
                if self.chosen_animal=="Elephants":
                    self.correct_ans=self.correct_ans+1
                
            #Panda
            elif which_animal==5:
                panda1=self.canvas.create_image(random.randint(50,710), random.randint(100,410), image=panda)
                if self.chosen_animal=="Pandas":
                    self.correct_ans=self.correct_ans+1
            
            #score_label needs to be passed through this function in order to be updated in the iscorrect function below
            self.RandomAnimals(label1, label2, button1, button2, tiger, zebra, lemur, elephant, panda, count-1, score_label)
    
    #Checks if given answer is correct
    def iscorrect(self, entry, score_label):
        given_ans=eval(entry.get())
        if given_ans==self.correct_ans:
            self.score=self.score+10 #User gets 10 points for a correct answer
        elif given_ans!=self.correct_ans:
            self.score=0 #The only other option is...0
    
        #Updates Score Display
        score_label.config(text=["Score:", self.score])
        
        #Runs endgame function
        self.endgame()
    
    #Displays popup that gives user the option to play again or return to main menu  
    def endgame(self):
        ##End of game display##
        popupmenu1=tk.Label(self.canvas, text=("Congratulations! You have completed the game. Your total score is"), font=("Courier", 11), anchor="n", bg="white", fg="black", height=7)
        popupmenu2=tk.Label(self.canvas, text=(self.score), font=("Courier", 11), anchor="n", bg="white", fg="red", height=7)
        popupmenu1.place(x=150, y=180)
        popupmenu2.place(x=610, y=180)
        #Play Again Button
        play_again=tk.Button(self.canvas, text="Play Again", bg="white", command= self.playagainbutton)
        play_again.place(x=295, y=240)
        #Return to Main Menu Button
        returnmenu=tk.Button(self.canvas, text="Main Menu", bg="white", command= self.returntomenu)
        returnmenu.place(x=395, y=240)
    
    #Plays the game again
    def playagainbutton(self):
        self.root.destroy() #Destroys the root in order to avoid making two windows
        root=tk.Tk() #Creates new root
        another=Animals(root) #Initializes game with new root
        another.gameplay() #Plays game again
        
    #Returns to Main Menu  
    def returntomenu(self):
        self.root.destroy() #Destroys the root in order to avoid making two windows
        returns=main_menu.Main_Menu() #Initializes main menu (Where a new root is created)
        returns.menu_graphics() #Runs main menu
