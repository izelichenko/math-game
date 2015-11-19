#equations.py
#Game 1 -- Equations -- Randomly generated equations show up on the screen and the user must submit their answer

import tkinter as tk
from tkinter import Frame
import random
import time
import main_menu

class Equations:
    
    def __init__(self, root, startx=320, starty=100):
        self.score=0 #Score Counter
        self.root=root #Using root created in main_menu
        self.correct_ans='' #Sets correct answer to empty string for now
       
    
    def game_window(self):
        ##Window##
        self.root.grid()
        self.root.title("Equations")
        ##Canvas##
        #Frame
        frame=Frame(self.root)
        frame.pack()
        self.canvas=tk.Canvas(frame, bg="white", width=800, height=500)
        self.canvas.pack()
        #Background/label
        bg_image=tk.PhotoImage(file="EQUATIONSbackground.gif")
        self.canvas.create_image(0, 250, image=bg_image, anchor="w")
        
        ##Score Display##
        score_label=tk.Label(self.root, text=["Score:", self.score], font=("Courier", 20), fg="red", bg="white")
        score_label.pack()
        score_label.place(x=650, y=450)
        
        ##Popup Menu##
        popupmenu=tk.Label(self.canvas, text=("Answer all eight equations correctly!"), font=("Courier", 12), anchor="n", bg="white", fg="black", height=7)
        popupmenu.place(x=280, y=180)
        #Return to Menu Button
        returnmenu=tk.Button(self.canvas, text="Main Menu", bg="white", command=self.returntomenu)
        returnmenu.place(x=425, y=240)
        #Start Button
        start=tk.Button(self.canvas, text="Start", bg="white")
        start.config(command= lambda: self.gameplay(popupmenu, start, returnmenu, score_label, 8))
        start.place(x=325, y=240)
                
        ##Keep running##
        self.root.mainloop()
    
    def gameplay(self, label, button1, button2, score_label, count):
        #Removes popup menu and buttons
        label.destroy()
        button1.destroy()
        button2.destroy()
        
        ##Generating Random Equations##
        which_eq=random.randint(1,4)
        ##For Addition##
        if which_eq==1:
            randint1=random.randint(0,25)
            randint2=random.randint(0,25)
            #Equation Answer
            AddEqAns=randint1+randint2
            self.correct_ans=AddEqAns #Sets correct answer to this answer
            #Equation String to be displayed on screen
            AddEqStr=str(randint1)+" + "+str(randint2)
            #Creating the Equation String as text on the screen
            EqText=self.canvas.create_text(400, 250, text=AddEqStr, font=("Courier", 40), fill="red")
        
        ##For Subtraction##    
        elif which_eq==2:
            randint1=random.randint(0,25)
            randint2=random.randint(0,25)
            #Equation Answer
            SubEqAns=randint1-randint2
            self.correct_ans=SubEqAns #Sets correct answer to this answer
            #Equation String to be displayed
            SubEqStr=str(randint1)+" - "+str(randint2)
            #Creating the Equation String as text on the screen
            EqText=self.canvas.create_text(400, 250, text=SubEqStr, font=("Courier", 40), fill="red")
        
        ##For Multiplication##    
        elif which_eq==3:
            randint1=random.randint(0,12)
            randint2=random.randint(0,12)
            #Equation Answer
            MultEqAns=randint1*randint2
            self.correct_ans=MultEqAns #Sets correct answer to this answer
            #Equation String to be displayed
            MultEqStr=str(randint1)+" x "+str(randint2)
            #Creating the Equation String as text on the screen
            EqText=self.canvas.create_text(400, 250, text=MultEqStr, font=("Courier", 40), fill="red")
        
        ##For Division##
        elif which_eq==4:
            randint1=random.randint(0,12)
            randint2=random.randint(0,12)
            #Equation Answer
            Integer=randint1*randint2
            DivEqAns=randint2
            self.correct_ans=DivEqAns #Sets correct answer to this answer
            #Equation String to be displayed
            DivEqStr=str(Integer)+" / "+str(randint1)
            #Creating the Equation String as text on the screen
            EqText=self.canvas.create_text(400, 250, text=DivEqStr, font=("Courier", 40), fill="red")
            
            
        ##Entry for Answer##
        #Label "total"
        total_label=tk.Label(self.root, text="Answer:", bg="white")
        total_label.place(x=255, y=410)
        #Actual entry bar
        total_entry=tk.Entry(self.root)
        total_entry.place(x=315, y=409)
        #Submit answer button
        total_submit=tk.Button(self.root, text="Submit", bg="white", command=lambda: self.iscorrect(label, button1, button2, total_entry, score_label, EqText, count))#, self.gameplay(label, button, score_label)])
        total_submit.place(x=490, y=404)
        
        #If 8 equations have been answered, End Game
        if count==0:
            return self.endgame(total_label, total_entry, total_submit)
    
    #Checks if entered answer is correct
    def iscorrect(self, label, button1, button2, entry, score_label, EqText, count):
        given_ans=eval(entry.get())
        if given_ans==self.correct_ans:
            self.score=self.score+5 #If it is, user gets 5 points
        elif given_ans!=self.correct_ans and self.score>0: #If wrong and score>0
            self.score=self.score-5 #User loses 5 points
        
        #Updates Score Label
        score_label.config(text=["Score:", self.score])
        
        #Delete current equation to make room for next one
        self.canvas.delete(EqText)
        
        #Print next equation (decreasing count by one to keep track of how many are created)
        self.gameplay(label, button1, button2, score_label, count-1)
    
    #Displays popup that gives user the option to play again or return to main menu  
    def endgame(self, label, entry, button):
        #Destroys label, entry, and submit botton **This currently does not work, but I'm keeping it here to work on later**
        label.destroy()
        entry.destroy()
        button.destroy()
        
        ##End of game display##
        popupmenu1=tk.Label(self.canvas, text=("Congratulations! You have completed the game. Your total score is"), font=("Courier", 11), anchor="n", bg="white", fg="black", height=7)
        popupmenu2=tk.Label(self.canvas, text=(self.score), font=("Courier", 11), anchor="n", bg="white", fg="red", height=7)
        popupmenu1.place(x=160, y=180)
        popupmenu2.place(x=600, y=180)
        #Play Again Button
        play_again=tk.Button(self.canvas, text="Play Again", bg="white", command= self.playagainbutton)
        play_again.place(x=295, y=240)
        #Return to Menu Button
        returnmenu=tk.Button(self.canvas, text="Main Menu", bg="white", command= self.returntomenu)
        returnmenu.place(x=395, y=240)
    
    #Plays the game again
    def playagainbutton(self):
        self.root.destroy() #Destroys the root in order to avoid making two windows
        root=tk.Tk() #Creates new root
        another=Equations(root) #Initializes Equations game with new root
        another.game_window() #Plays the game
        
    #Returns to Main Menu     
    def returntomenu(self):
        self.root.destroy() #Destroys the root in order to avoid making two windows
        returns=main_menu.Main_Menu() #Initializes main menu (where a new root is created)
        returns.menu_graphics() #Runs main menu


