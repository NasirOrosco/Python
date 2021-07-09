'''
Created on Jul 8, 2021

@author: Nasir Orosco
'''
'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''

#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''

'''
#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.
def math(int1,int2):
    answer= int1-int2
    return answer

int1=input("INSERT #")
int1=int(int1)
int2=input("INSERT #")
int2=int(int2)
print(math(int1, int2))
#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.
def math2(solution):
    answer=solution/2*77+10000
    return answer
solution=input("INSERT #")
solution=int(solution)
print(math2(solution))

#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.

def math3(num1,num2):
    if(num1==num2):
        return True
    else:
        return False
    
num1=input("Please insert a #")
num1=int(num1)
num2=input("Please insert the same # as before")
num2=int(num2)
print(math3(num1,num2))


#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.
def math4(num3,num4):
    if(num3>num4):
        return num3 
    if(num3<num4):
        return num4
    if(num3==num4):
        return "equal"
    
    
num3=input("Please insert a #")
num3=int(num3)
num4=input("Please insert a #")
num4=int(num4)
print(math4(num3,num4))


#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.
def math5(str1,str2):
    answer= str1+str2
    return answer

int1=input("INSERT #")
int2=input("INSERT #")
print(math5(int1, int2))
'''

#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.
def math6(num5,num6,num7):
    if(num5==num6) or (num5==num7):
        return True 
    else:
        return False
    
    
num5=input("Please insert a #")
num5=int(num5)
num6=input("Please insert a #")
num6=int(num6)
num7=input("Please insert a #")
num7=int(num7)
print(math6(num5,num6,num7))


#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.



#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.



#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.
