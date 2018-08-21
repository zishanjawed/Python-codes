import math
"""
program : Calculate the sum of the area of a regular polygon and square of it's perimeter 


@author : ZISHAN JAWED
"""
def polysum(n, s):
	"""
	input : Number of sides 'n ', lenght of sides 's'
	
	output : return sum of the area and square of perimetrer which is round by four decimal places 
	"""
	
	# Claculating the area of regular polygon i.s (0.25 * n* s)/ tan(pi/n)
    area = (0.25 * n * s**2) / (math.tan(math.pi/n))

    #Calulatin the sqare of the perimeter , perimeter : s * n 
    perimeter = (n * s)**2

    # Adding the area with the square of the perimeter
    Sum = area + perimeter
    
    return round(Sum, 4)

print(polysum(56,13))