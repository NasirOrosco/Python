'''
Created on Jul 1, 2021

@author: Nasir Orosco
'''
'''
The following function has problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with
CONDITIONAL STATEMENTS.
Focus on the conditional statements and find the problems with 
the CONDITIONAL STATEMENTS.

fixMyCar has 10 errors
'''

'''
The following function takes in a problem and compares it to 
different car problems in it's database. Depending on the problem
it gives a solution to fix the car.

It should only print out ONE solution(it should be one if statement, multiple
elif statements, and one else statement).

If the problem is: tire, it says: Replace tires.

If the problem is: headlight, it says: Fill headlight fluid.

If the problem is: door, it says: replace door.

If the problem is: gas, it says: Fill gas tank.

If the problem is: window, it says: Replace window.

If the problem is: wipers, it says: Replace windshield wipers.

If the problem is: battery, it says: Replace battery.

If the problem is: exhaust, it says: Replace exhaust system.

If the problem is: transmission, it says: Throw out car.

If the problem is: anything else, it says: Your car is fine.
'''
def fixMyCar(problem):
    if(problem == "tire"):
        print("Replace tires")
    elif(problem=="headlight"):
        print("Fill headlight fluid.")
    elif(problem == "door"):
        print("replace door")
    elif(problem == "gas"):
        print("Fill gas tank")
    elif(problem == "window"):
        print("Replace window")
    elif(problem == "wipers"):
        print("Replace windshield wipers")
    elif(problem == "battery"):
        print("Replace battery")
    elif(problem == "exhaust"):
        print("Replace exhaust system")
    elif(problem == "transmission"):
        print("Throw out car")
    else:
        (problem=="anything else")
        print("Your car is fine")
    
    return 

fixMyCar("tire")
fixMyCar("headlight")
fixMyCar("door")
fixMyCar("gas")
fixMyCar("window")
fixMyCar("wipers")
fixMyCar("battery")
fixMyCar("exhaust")
fixMyCar("transmission")
fixMyCar("Nothing")