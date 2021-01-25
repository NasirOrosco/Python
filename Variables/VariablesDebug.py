def volumeCalculator(height, width, depth):
    
    area = height * width
    
    volume = depth * area
    
    sentence = "The volume of this object is:"
    
    print([sentence]+[volume])
    
    return(volume) 

#Leave the next line alone
volumeCalculator(5, 5, 5)

def shippingAndTax(subTotal):
    shipping = 10
    tax = .10
    
    taxTotal = subTotal * tax
    total = subTotal + taxTotal + shipping
    print("The total is: " + total)
    return total

#Leave the next line alone
shippingAndTax(15)

def circleArea(radius):
    pi = 3.14
    squared = radius * radius
    area = pi * squared 
    
    print("The area is: " + area)
    return area

#Leave the next line alone
circleArea(5)