# math-game
Math Games

Game Design

My game is built using the tkinter module and implements several programming techniques.

* All four files pertaining to the game contain a class. The Main Menu, the Equations game, the Perfect Squares game, and the Animals game are each their own class.
* Through import statements, these classes are allowed to interact with each other in order to seamlessly move between windows (Main Menu to Game and back).

Equations:
- The basic design of this game is to generate random equations and prompt the user to submit an answer.
- The main gameplay structure is comprised of four sections: addition, subtraction, multiplication, and division.
- Which of these four sections will be used for the next question is chosen randomly by using the random number module and generating a random number 1-4.
- Under each section a random equation using the given operation is put together. The equation is stored as a string to be displayed on screen, while the answer is assigned to a global variable to be checked against when the user submits their answer.
- Recursion is used under the iscorrect function, where self.gameplay is rerun with the “count” parameter set to “count-1” in order to assure that only 8 equations are printed.

Perfect Squares:
- The basic design of this game is to generate 10 buttons that display a random number that can either be a perfect square or not.
- The main gameplay structure consists of 10 sections, one for each button (A-J).
- Whether each button displays a perfect square or not is chosen randomly by using the random number module and generating a random number 0-1.
- If the button is chosen to display a perfect square, it randomly chooses one element from a previously generated list of 10 random perfect squares.
- If the button is chosen to display another number, it does the same thing from a previously generated list of 10 random other numbers.
- The program keeps track of how many perfect squares are created in order to be able to tell if the user has clicked on them all.
- A for loop is used in the iscorrect function in order to test out whether the correct button has been clicked (it loops through all the elements in the list of perfect squares).
- A for loop is also used in the endgame function to loop through all the buttons and remove them from the screen.

Animals:
- The basic design of this game is to generate 20 random animals and display them in random places on the screen.
- The main gameplay structure consists of 5 sections, one for each type of animal (tiger, lemur, elephant, panda, and zebra).
- One of these 5 animals is randomly chosen at the beginning to be the chosen animal that the user must count.
- Then, through the use of recursion, 20 instances of animals, randomly chosen among the 5, are displayed on the screen.
- Each time an instance of the chosen animal is created, a specific counter is incremented by 1. This allows the program to keep track of how many copies of the chosen animal are generated in order to be able to check against the user’s entered answer.

