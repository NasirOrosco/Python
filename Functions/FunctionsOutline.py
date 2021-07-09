'''
Created on Jul 7, 2021

@author: ITAUser
'''
'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.
def booleantrue(boo1, boo2):
    if (boo1==True) and (boo2==True):
        return True
    else:
        return False

boo1=(5>4)
boo2=(5>1)
print(booleantrue(boo1, boo2))
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def galtocups(gallons):
    cups= gallons*16
    return cups
print(galtocups(5))

#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.

def milestofeet(miles)
    feet= miles*5280
    return feet
print(milestofeet(5))
