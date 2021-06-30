'''
Created on Jun 29, 2021

@author: ITAUser
'''
#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.
miles = input("Number Of Miles?")
#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
#
#Store the value in a variable called yards and print it out with a 
#simple statement.
yards = int(miles) * 1760
print(str(miles) + " miles converts to " + str(yards)+"yards")
#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
#
#Store the value in a variable called feet and print it out with a 
#simple statement.
Feet= int(miles) * 5280
print(str(miles) + " miles converts to "+ str(Feet)+"feet")
#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
#
#Store the value in a variable called inches and print it out with a 
#simple statement.
Inches= int(miles)*63360
print(str(miles) + " miles converts to " + str(Inches)+"inches")