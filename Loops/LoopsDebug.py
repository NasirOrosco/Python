'''
Created on Jul 7, 2021

@author: Nasir Orosco
'''
'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with LOOPS.
Focus on the loops and find the problems with the LOOPS.

The number of errors are as follows:
counting: 4
fruits: 3
checkStudents: 3
printGrades: 2
'''

'''
This function uses a while loop to print out every number from
1 to 100.
'''
def counting():
    x = 0
    while(x <= 100):
        print(x)
        x = x + 1
    print("DONE")
    return 

counting()

'''
This function takes a list of fruits and prints out each fruit in the list using
a for loop.
'''
def fruits(fruit):
    for x in fruit:
        print(x)
    print("DONE")
    return 

listOFruit = ["apple", "pear", "peach", "watermelon", "tomato"]
fruits(listOFruit)


'''
This function takes an input of a 2D list. In the first dimension, it's a string 
list of the student names. In the second dimension, it's a boolean list of 
whether or not the student is failing.
The function then goes through the list and prints whether or not the student is 
passing and or not. If the student is passing, it prints "[NAME] is passing." If
the student is failing, it prints "[NAME] is failing."
'''
def checkStudents(studentList):
    x = 0
    while(x <= len(studentList[0])):
        if(studentList[1][x] == True):
            print(studentList[0][x] + " is passing.")
        else:
            print(studentList[0][x] + " is failing.")
        x = x+1
    print("DONE")
    return


listOfStudents = [["Michael", "Patrice", "Amaya", "William"], [True, True, True, False]]
checkStudents(listOfStudents)

'''
This function takes a list of grades and then prints each of the grades out with
a for loop.
'''
def printGrades(studentList):
    for grade in listOfStudents :
        print(grade)
    print("DONE")
    return 

listOfStudents = [66, 24, 12, 45, 100, 100, 100]
printGrades(listOfStudents)