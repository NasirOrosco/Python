'''
Created on Dec 5, 2020

@author: ITAUser
'''
def circleArea():
    radius = input("What is the radius of your circle?")
    
    pi = 3.14
    squared = int(radius) * int(radius)
    area = pi * squared 
    print("The area is: " + area)
    return area

#Leave the next line alone
circleArea()

def rectangleArea():
    height = input("What is the height of your rectangle?")
    width = input("What is the width of your rectangle?")
    
    area = int(height) * int(width)
    print(area)
    return area

#Leave the next line alone
rectangleArea()
