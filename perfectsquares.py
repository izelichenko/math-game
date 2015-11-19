#perfectsquares.py
#Builds the Perfect Squares game (Game 2)
import tkinter as tk
from tkinter import Frame
import random
import time
import main_menu


class PerfectSquares:
    
    def __init__(self, root):
        self.score=0 #Score Counter
        self.root=root #Using root created in main_menu
        self.num_perf_sq=0 #Keeps track of number of perfect squares created 
        #Keeps track of number of perfect squares the user has clicked on
        #in order to know when to end the game
        self.num_correct=0 
        
    def game_window(self):
        #List of perfect squares
        list_squares=[]
        for i in range(1,13):
            list_squares.append(i**2)
        
        #List of other numbers    
        list_other_numbers=[]
        for i in range(1,145):
            if i!=list_squares[0] and i!=list_squares[1] and i!=list_squares[2] and i!=list_squares[3] and i!=list_squares[4] and i!=list_squares[5] and i!=list_squares[6] and i!=list_squares[7] and i!=list_squares[8] and i!=list_squares[9] and i!=list_squares[10] and i!=list_squares[11]:
                list_other_numbers.append(i)
        
        ##Window##
        self.root.grid()
        self.root.title("Perfect Squares")
        ##Canvas##
        #Frame        
        frame=Frame(self.root)
        frame.pack()
        self.canvas=tk.Canvas(frame, bg="white", width=800, height=500)
        self.canvas.pack()
        #Background/label
        bg_image=tk.PhotoImage(file="PERFECTSQUARESbackground.gif")
        self.canvas.create_image(0, 250, image=bg_image, anchor="w")
    
        ##Score Display##
        score_label=tk.Label(self.root, text=["Score:", self.score], font=("Courier", 20), fg="red", bg="white")
        score_label.pack()
        score_label.place(x=650, y=450)
        
        ##Popup Menu##
        popupmenu=tk.Label(self.canvas, text=("Click on all the perfect squares!"), font=("Courier", 12), anchor="n", bg="white", fg="black", height=7, borderwidth=16)
        popupmenu.place(x=295, y=180)
        #Return to Menu Button
        returnmenu=tk.Button(self.canvas, text="Main Menu", bg="white", command=self.returntomenu)
        returnmenu.place(x=425, y=265)
        #Start Button
        start=tk.Button(self.canvas, text="Start", bg="white")
        start.config(command= lambda: self.gameplay(popupmenu, start, returnmenu, list_squares, list_other_numbers, score_label))
        start.place(x=325, y=265)
        
        ##Keep running##
        self.root.mainloop() 
    
    def gameplay(self, label, button1, button2, list_squares, list_other_numbers, score_label):   
        #Removes popup menu and buttons
        label.destroy()
        button1.destroy()
        button2.destroy()
        
        ##Options##
        #Perfect squares
        #10 variables for 10 buttons (accounting for the chance that all 10 will have perfect squares)
        a=list_squares[random.randint(0,11)]
        b=list_squares[random.randint(0,11)]
        c=list_squares[random.randint(0,11)]
        d=list_squares[random.randint(0,11)]
        e=list_squares[random.randint(0,11)]
        f=list_squares[random.randint(0,11)]
        g=list_squares[random.randint(0,11)]
        h=list_squares[random.randint(0,11)]
        i=list_squares[random.randint(0,11)]
        j=list_squares[random.randint(0,11)]
        #List from which to choose how many of the ten buttons will have perfect squares
        list_chose_sq=[a, b, c, d, e, f, g, h, i, j]
        
        #Other numbers
        #10 variables for 10 buttons (accounting for the chance that all 10 will have other numbers)
        k=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        l=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        m=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        n=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        o=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        p=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        q=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        r=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        s=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        t=list_other_numbers[random.randint(0,(len(list_other_numbers)-1))]
        #List from which to choose how many of the ten buttons will have other numbers
        list_chose_other=[k, l, m, n, o, p, q, r, s, t]
        
        ##Buttons with options##
        ##There is a 50% chance that a button will have a perfect square##
        ##There is a 50% chance that a button will have another number##
        ##These numbers are then chosen randomly from the lists above##
        #ButtonA
        if random.randint(0,1)==0:
            buttonAtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonAtext=str(list_chose_other[random.randint(0,9)])
        buttonA=tk.Button(self.root, text=buttonAtext, fg="dark red", bg="white", width=10, font="bold")
        buttonA.place(x=50, y=100)
        
        #ButtonB
        if random.randint(0,1)==0:
            buttonBtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonBtext=str(list_chose_other[random.randint(0,9)])
        buttonB=tk.Button(self.root, text=buttonBtext, fg="dark blue", bg="white", width=10, font="bold")
        buttonB.place(x=250, y=100)
        
        #ButtonC
        if random.randint(0,1)==0:
            buttonCtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonCtext=str(list_chose_other[random.randint(0,9)])
        buttonC=tk.Button(self.root, text=buttonCtext, fg="dark green", bg="white", width=10, font="bold")
        buttonC.place(x=450, y=100)
        
        #ButtonD
        if random.randint(0,1)==0:
            buttonDtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonDtext=str(list_chose_other[random.randint(0,9)])
        buttonD=tk.Button(self.root, text=buttonDtext, fg="black", bg="white", width=10, font="bold")
        buttonD.place(x=650, y=100)
        
        #ButtonE
        if random.randint(0,1)==0:
            buttonEtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonEtext=str(list_chose_other[random.randint(0,9)])
        buttonE=tk.Button(self.root, text=buttonEtext, fg="blue", bg="white", width=10, font="bold")
        buttonE.place(x=150, y=200)
        
        #ButtonF
        if random.randint(0,1)==0:
            buttonFtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonFtext=str(list_chose_other[random.randint(0,9)])
        buttonF=tk.Button(self.root, text=buttonFtext, fg="pink", bg="white", width=10, font="bold")
        buttonF.place(x=350, y=200)
        
        #ButtonG
        if random.randint(0,1)==0:
            buttonGtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonGtext=str(list_chose_other[random.randint(0,9)])
        buttonG=tk.Button(self.root, text=buttonGtext, fg="red", bg="white", width=10, font="bold")
        buttonG.place(x=550, y=200)
        
        #ButtonH
        if random.randint(0,1)==0:
            buttonHtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonHtext=str(list_chose_other[random.randint(0,9)])
        buttonH=tk.Button(self.root, text=buttonHtext, fg="green", bg="white", width=10, font="bold")
        buttonH.place(x=50, y=300)
        
        #ButtonI
        if random.randint(0,1)==0:
            buttonItext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonItext=str(list_chose_other[random.randint(0,9)])
        buttonI=tk.Button(self.root, text=buttonItext, fg="black", bg="white", width=10, font="bold")
        buttonI.place(x=350, y=300)
        
        #ButtonJ
        if random.randint(0,1)==0:
            buttonJtext=str(list_chose_sq[random.randint(0,9)])
            self.num_perf_sq=self.num_perf_sq+1
        else:
            buttonJtext=str(list_chose_other[random.randint(0,9)])
        buttonJ=tk.Button(self.root, text=buttonJtext, fg="purple", bg="white", width=10, font="bold")
        buttonJ.place(x=650, y=300)
        
        ##List of buttons. Used to delete them from the screen when the game is over##
        list_buttons=[buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG, buttonH, buttonI, buttonJ]
        
        ##Change all the buttons to check correct answer##
        ##We need to do this here so we can include the list of buttons in the parameters##
        buttonA.config(command=lambda: self.iscorrect(buttonA, list_squares, list_other_numbers, score_label, list_buttons))
        buttonB.config(command=lambda: self.iscorrect(buttonB, list_squares, list_other_numbers, score_label, list_buttons))
        buttonC.config(command=lambda: self.iscorrect(buttonC, list_squares, list_other_numbers, score_label, list_buttons))
        buttonD.config(command=lambda: self.iscorrect(buttonD, list_squares, list_other_numbers, score_label, list_buttons))
        buttonE.config(command=lambda: self.iscorrect(buttonE, list_squares, list_other_numbers, score_label, list_buttons))
        buttonF.config(command=lambda: self.iscorrect(buttonF, list_squares, list_other_numbers, score_label, list_buttons))
        buttonG.config(command=lambda: self.iscorrect(buttonG, list_squares, list_other_numbers, score_label, list_buttons))
        buttonH.config(command=lambda: self.iscorrect(buttonH, list_squares, list_other_numbers, score_label, list_buttons))
        buttonI.config(command=lambda: self.iscorrect(buttonI, list_squares, list_other_numbers, score_label, list_buttons))
        buttonJ.config(command=lambda: self.iscorrect(buttonJ, list_squares, list_other_numbers, score_label, list_buttons))
        
    #Checks if clicked button contains perfect square  
    def iscorrect(self, button, list_squares, list_other_numbers, score_label, list_buttons):
        for i in range(len(list_squares)):
            if button['text']==str(list_squares[i]):
                self.score=self.score+5 #If it is, user gets 5 points
                self.num_correct=self.num_correct+1 #And 1 is added to how many they have clicked correctly
                
                
        for i in range(len(list_other_numbers)):
            if button['text']==str(list_other_numbers[i]) and self.score>0: #If other number and score>5
                self.score=self.score-5 #User loses 5 points
        
        #Disables buttons so you can't click it twice
        button.config(state="disabled")
        #Updates Score Display
        score_label.config(text=["Score:", self.score])
        
        #If the user has already clicked on all the perfect squares
        if self.num_perf_sq==self.num_correct:
            return self.endgame(list_buttons) #End Game
            
     #Displays popup that gives user the option to play again or return to main menu
    def endgame(self, list_buttons):
        #Destroys all the buttons to clear the canvas
        for e in list_buttons:
            e.destroy()
        ##End of game display##
        popupmenu1=tk.Label(self.canvas, text=("Congratulations! You have completed the game. Your total score is"), font=("Courier", 11), anchor="n", bg="white", fg="black", height=7)
        popupmenu2=tk.Label(self.canvas, text=(self.score), font=("Courier", 11), anchor="n", bg="white", fg="red", height=7)
        popupmenu1.place(x=150, y=180)
        popupmenu2.place(x=610, y=180)
        #Play Again
        play_again=tk.Button(self.canvas, text="Play Again", bg="white", command= self.playagainbutton)
        play_again.place(x=295, y=240)
        #Return to Menu
        returnmenu=tk.Button(self.canvas, text="Main Menu", bg="white", command= self.returntomenu)
        returnmenu.place(x=395, y=240)
    
    #Plays the game again
    def playagainbutton(self):
        self.root.destroy() #Destroys the root in order to avoid making two windows
        root=tk.Tk() #Creates new root
        another=PerfectSquares(root) #Initializes game with new root
        another.game_window() #Plays game again
        
    #Returns to Main Menu 
    def returntomenu(self):
        self.root.destroy() #Destroys the root in order to avoid making two windows
        returns=main_menu.Main_Menu() #Initializes main menu (Where a new root is created)
        returns.menu_graphics() #Runs main menu
        

        

        
