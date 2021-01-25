'''
Created on Dec 4, 2020

@author: NasirOrosco
'''

'''
The goal of this function is to calculate the volume of
an object, when the user inputs height, width, and depth.

The function should print the sentence plus the volume and
return the volume.'''

def volumeCalculator(height, width, depth):
    area = height * width
    volume = depth * area
    sentence = "The volume of this object is: "
    #This prints out the sentence with the calculated volume.
    print(sentence + volume)
    return volume

#Leave the next line alone
volumeCalculator(5, 5, 5)