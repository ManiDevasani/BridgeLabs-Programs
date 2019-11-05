"""""
----------------------------------------------------------------------------------------------------
 Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
----------------------------------------------------------------------------------------------------

"""

class Distance:
    def calculation(self):
        import math
        # taking the points from the user
        print("Enter the x value")
        x = int(input())
        print("Enter the y value")
        y = int(input())
        print("The diatance between th origin and the given points(",x,",",y,") is :")
        # calculating the distanc eusing the given formula 'distance = sqrt(x*x + y*y).' and print the distance values
        x = x*x
        y = y*y
        distance = x+y
        distance = math.sqrt(distance)
        print(distance)
dist = Distance()
dist.calculation()