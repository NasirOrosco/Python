'''
Created on Jun 30, 2021

@author: Nasir Orosco
'''
'''
The following function has problems that keep it from
completing the task that it has to do.

All the problems are either Logical or Syntactical errors with LOGICAL OPERATORS.
Focus on the logical operators and find the problems with the LOGICAL OPERATORS.

The problems can be: operators that are there but shouldn't be, operators
that are misspelled, operators that are the incorrect operators.

The number of errors are as follows:
checkWhoWins: 6 errors
'''
import random

'''
This function checks who won in a rock paper scissor game, between a human
and the cpu.

The computer makes a random choice(1 through 3).

The function compares choice(the users choice) to cpuChoice(the computers
choice) and prints who wins or if it is a draw.
'''
def checkWhoWins(choice):
    '''
    cpuChoice is a number 1-3, the number corresponds to an answer:
    1 = rock
    2 = scissors
    3 = paper
    '''
    cpuChoice = random.randint(1,2,3)
    
    # This condition checks if there is a draw
    if((choice == 'rock' and cpuChoice == 1)  (choice == 'scissors' and cpuChoice == 2)
        or (choice == 'paper' and cpuChoice == 3)):
        print("DRAW!")
    
    # This condition checks if the human wins
    if((choice == 'rock' and cpuChoice == 2) or (choice == 'scissors' and cpuChoice == 3)
        or (choice == 'paper' and  cpuChoice == 1)):
        print("HUMAN WINS!")
    
    # This condition checks if the cpu wins
    if((choice == 'rock' and cpuChoice == 3) or (choice == 'scissors' and cpuChoice == 1)
        or (choice == 'paper' and cpuChoice == 2)):
        print("CPU WINS!")
    
    return

checkWhoWins("rock")
checkWhoWins("paper")
checkWhoWins("scissors")