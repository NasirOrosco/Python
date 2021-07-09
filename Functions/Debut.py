'''
Created on Jul 8, 2021

@author: Nasir Orosco
'''
'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with FUNCTIONS.
Focus on the functions and find the problems with the FUNCTIONS.

For this debug, there could be problems with executing the functions. For example,
calling the function may have been done wrong, or put in the wrong spot. So don't
just look at the function itself but also the line calling the function.

Additionally, if converting becomes difficult, ask the instructor about how to
use a conversion table or other tricks to help make sure the conversion is right.

The number of errors are as follows:
ouncesToGallons: 4
gallonsToOunces: 5
gramsToPounds: 4
poundsToGrams: 4
'''

#1) The problem starts after this line-----------------------------------------
#HINT: Should this line be here?

'''
This function converts ounces to gallons using three steps. It takes one
integer parameter: ounces.
First, it converts ounces to cups.
Second, converts cups to quarts.
Third, converts quarts to gallons.
Finally, it returns gallons.
'''
def ouncesToGallons(ounces):
    #There are eight ounces in a cup
    cups = ounces / 8
    
    #There are four cups in a quart
    quarts = cups / 4
    
    #There are four quarts in a gallon
    gallons = quarts / 4
    
    return gallons

ouncesToGallons(24)
#END OF PROBLEM 1--------------------------------------------------------------


#2) The problem starts after this line-----------------------------------------
'''
This function converts gallons to ounces using three steps. It takes one
integer parameter: gallons.
First, it converts gallons to quarts.
Second, converts quarts to cups.
Third, converts cups to ounces.
Finally, it returns ounces.
'''
def gallonsToOunces(gallons):
    #There are four quarts in a gallon
    quarts = gallons * 4
    
    #There are four cups in a quart
    cups = quarts * 4
    
    #There are 8 ounces in a cup
    ounces = cups * 8
    
    return ounces

gallonsToOunces(24)

#END OF PROBLEM 2--------------------------------------------------------------


#3) The problem starts after this line-----------------------------------------
'''
This function converts grams to pounds using two steps. It takes one integer
parameter: grams.
First, it converts grams to ounces.
Second, it converts ounces to pounds.
Then it returns pounds.
'''
def gramsToPounds(grams):
    #There are .035 ounces in a gram
    ounces = grams / .035
    #There are 16 ounces in one pound
    pounds = ounces / 16
    
    
    return pounds


gramsToPounds(360)

#END OF PROBLEM 3--------------------------------------------------------------


#4) The problem starts after this line-----------------------------------------
'''
This function converts pounds to grams using two steps. It takes one integer
parameter: pounds.
First, it converts pounds to ounces.
Second, it converts ounces to grams.
Then it returns grams.
'''
def poundsToGrams(pounds):
    #There are 16 ounces in one pound
    ounces = pounds * 16
    
    #There are .035 ounces in a gram
    grams = ounces * .035
    
    return grams


poundsToGrams (360)

#END OF PROBLEM 4--------------------------------------------------------------