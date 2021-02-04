'''
Created on Feb 3, 2021

@author: ITAUser
'''
'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with 
COMPARISON OPERATORS.
Focus on the comparison operators and find the problems with 
the COMPARISON OPERATORS.

The number of errors are as follows:
comparisonDrill: 3
comparisonDrillTwo: 1
shippingAndTax: 3
'''


'''
This function compare a to b.

-If a is less than b, the function prints "A is less than B."
-If a is equal to b, the function prints "A is equal to B."
-If a is more than b, the function prints "A is greater than B."
'''
def comparisonDrill(a, b):
    if(a >= b):
        print("A is greater than B.")
    elif(a == b):
        print("A is equal to B.")
    elif(a <= b):
        print("A is less than B.")
    
    return 

comparisonDrill(2, 3)
comparisonDrill(3, 3)
comparisonDrill(4, 3)

'''
This function compares userTest to correctAnswer

-If the variables are the same, the function prints "CORRECT!"
'''
def comparisonDrillTwo(userText, correctAnswer):
    if(userText == correctAnswer):
        print("CORRECT!")
    
    return 

comparisonDrillTwo("YES", "YES")
comparisonDrillTwo("NO", "YES")

'''
The goal of this function is to calculate the 
total of an order after tax and shipping.

-If the subtotal is less than 15, the function makes shipping 5.
-If the subtotal is more or equal to 15, the function makes shipping 10.
-If the subtotal is more than 100, the function makes shipping 0.

The function should print and
return the total
'''
def shippingAndTax(subtotal):
    shipping = 0
    tax = .10
    
    if(subtotal == 15):
        shipping = 5
    if(subtotal >= 15):
        shipping = 10
    if(subtotal >= 100):
        shipping = 0
    
    taxTotal = subtotal * tax
    total = subtotal + taxTotal + shipping
    print("The total is: ", total)
    return total

shippingAndTax(10)
shippingAndTax(15)
shippingAndTax(20)
shippingAndTax(101)