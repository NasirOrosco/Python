'''
Created on Jun 29, 2021

@author: ITAUser
'''
'''
This outline will help solidify concepts from the Logical Operators lesson.
Fill in this outline as the instructor goes through the lesson.
'''
#EX) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.
one = True
two = False
a = one and two 
print(a)

#1) Make two boolean variables. Put them on either side of the and operator.
#Store this expression in a variable named a. Print the variable.
FirstName="Nas"
LastName="Orosco"
A= (FirstName=="Nas") and (LastName=="Orosco") 
print(A)
#2) Make two boolean variables. Put them on either side of the or operator.
#Store this expression in a variable named b. Print the variable.
b=(FirstName=="Nasir") or (LastName=="Orosco")
print(b)
#3) Make one boolean variable. Put the variable after the not. Store this 
#expression in a variable named c. Print the variable.
MiddleName="X"
c=not MiddleName=="X"
print(c)
#4) Make a logical expression with one of the common SYNTAX errors.
5==5 and 9=9
