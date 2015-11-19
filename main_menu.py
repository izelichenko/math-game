#Actual Game design using tkinter

import tkinter as tk
import equations
import perfectsquares
import animals
from tkinter import Frame
import time

class Main_Menu:
  
  def __init__(self):
    self.width=800 #Window width
    self.height=500 #Window height
    self.root=tk.Tk() #Define root
    
  def menu_graphics(self):
    ##Window##
    self.root.grid()
    #Name of window
    self.root.title("Main Menu")
    
    ##Canvas##
    self.canvas=tk.Canvas(self.root, bg="white", width=self.width, height=self.height)
    self.canvas.pack()
    #Background/label
    label_image=tk.PhotoImage(file="MATHbackground.gif")
    label=tk.Label(self.root, image=label_image)
    label.place(x=0, y=0, relwidth=1, relheight=1)
    #Equations Game Button
    EqButton=tk.PhotoImage(file="EquationsButton.gif")
    b=tk.Button(self.root, image=EqButton, fg="red", command=self.PlayEquations)
    b.place(x=135, y=75)
    #Perfect Squares Game Button
    PSButton=tk.PhotoImage(file="PerfectSquaresButton.gif")
    b=tk.Button(self.root, image=PSButton, fg="red", command=self.PlayPerfectSquares)
    b.place(x=435, y=75)
    #Animals Game Button
    AnButton=tk.PhotoImage(file="AnimalsButton.gif")
    b=tk.Button(self.root, image=AnButton, fg="red", command=self.PlayAnimals)
    b.place(x=280, y=225)
    #Help Button **This does not have a function yet, but is supposed to link to instructions of each game**
    #HelpButton=tk.PhotoImage(file="HelpButton.png")
    #b=tk.Button(self.root, image=HelpButton, fg="red")
    #b.place(x=740, y=440)
    
    ##Keep running##
    self.root.mainloop()
    
  def PlayEquations(self):
    self.canvas.destroy() #Clears current canvas
    game_start=equations.Equations(self.root) #Initializes an Equations game using current root
    game_start.game_window() #Plays the game

  def PlayPerfectSquares(self):
    self.canvas.destroy() #Clears current canvas
    game_start=perfectsquares.PerfectSquares(self.root) #Initializes a Perfect Squares game using current root
    game_start.game_window() #Plays the game
  
  def PlayAnimals(self):
    self.canvas.destroy() #Clears current canvas
    game_start=animals.Animals(self.root) #II
    game_start.gameplay()
  
  
disp=Main_Menu()
disp.menu_graphics()
