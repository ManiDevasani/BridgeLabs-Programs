"""""
-----------------------------------------------------------------------------------------
Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots.
----------------------------------------------------------------------------------------
"""
class Quadratic:
    def number(self):
        import math
        # taking input a,b,c values from user
        print("Enter A value")
        a = int(input())
        print("Enter B value")
        b = int(input())
        print("Enter C value")
        c = int(input())
        print("Roots of the equation(",a,")x2 + (",b,")x + (",c,") is")
        # By using the given formulas calculate the roots of the equation with given values
        delta = b*b - 4*a*c
        root1 = (-b + math.sqrt(delta))/(2*a)
        root2 = (-b - math.sqrt(delta))/(2*a)
        print("Root 1 :",root1)
        print("Root 2 :",root2)
roots = Quadratic()
roots.number()
