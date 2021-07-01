'''
Created on Jul 1, 2021

@author: Nasir Orosco
'''
#1) Create a Variable called grade and set it to an integer. Make an 
#if/elif/else statement. If grade is equal to or above 80, then print "passing".
#Elif grade is lower than 80 and greater than or equal to 60, then print
#"probation". Else, print "failing". 
grade=95
if(grade>=80):
    print("PASSING")
elif(grade<80) or (grade>=60):
    print("PROBATION")
else:
    print("FAILING")
#2) Make a int variable named a. Now make an if/elif statment, and if a is more
#than/equal too 100 or less than/equal too -100, print "a is a three digit 
#number". Elif a is between 100 and -100, print "a is not a three digit number".
a=57
if(a>=100) or (a<=-100):
    print("a is a three digit number")
elif(a<100) or (a>-100):
    print("a is not a three digit number")

#3)Create a variable called age. Make an if/else statement. If age is older
#than 18, print "You can vote". Else, print "You cannot vote".
age=18
if(age>=18):
    print("YOU CAN VOTE")
else:
    (age<18)
    print("YOU CAN NOT VOTE")    
    
#4)Make a string variable called answer, and set it to the letter a, b, c, or d.
#Make an if/elif statement. If answer is a, b, or d, print "Wrong". Elif answer
#is c, print "Correct".
answer="c"
if(answer=="a,b, or ,d"):
    print("WRONG")
elif(answer=="c"):
    print("CORRECT")



#5)Make two boolean variables. Make an if/elif/else statement. If both booleans 
#are true, print "Both". Elif only one of the booleans is true, print "Only 
#one". Else, print "Neither".
Boolean= (5==5)
boolean= (2==2)
if(boolean==True) and (Boolean==True):
    print("Both")
elif(boolean==True) and (Boolean==False):
    print("Only One")
else:
    print("Neither")