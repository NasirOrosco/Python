'''
Created on Jul 1, 2021
The purpose is too create a quiz that tests people's basic highschool knowledge.
@author: Nasir
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score=0
#Ask the user question one. And store the users answer.
question1=input("What is the powerhouse of the cell?    a) mitochondria b) nucleus c) ribosome")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(question1.lower()=="a"):
    score=+1
    print("Correct")
else:
    print("Incorrect, correct answer is a.")
#Ask the user question two. And store the users answer.
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
question2=input("2) How many states comprise the United States?  a) 13 b) 45 c) 50")
if(question2.lower()=="c"):
    score=score+1
    print("Correct")
else:
    print("Incorrect, answer is c.")
#Ask the user question three. And store the users answer.
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
question3= input("3) In y = mx + b, what does m stand for?  a) slope b) output c) I don't understand math")
if(question3.lower()=="a"):
    score= score+1
    print("Correct")
else:
    print("Incorrect, answer is a.")
#Ask the user question four. And store the users answer.
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
question4=input("4) In English, a person, place or thing is called?  A) verb B) adjective C) noun")
if(question4.lower()=="c"):
    score=score+1
    print("Correct")
else:
    print("Incorrect, answer is c.")

#Calculate the percentage the user got. And store it in a variable called p
p= (int(score)/4)*100
#Print out the users score: "You got a [score]/4. Or a [p]%."
print(f"Yout got a {p}%")