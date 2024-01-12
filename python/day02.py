# Create a program to calculate the area of a circle given its radius.

# Import numpy for pi value
import numpy as np 

# Write function that calculates and returns area of a cirlce given radius
def area_circle(r):

    area_circle = np.pi * r ** 2
    print("Area of a circle with radius of", r, "=", round(area_circle,2))

# Prompt user to provide radius
r = float(input('Enter radius:'))

# Run function
area_circle(r)
