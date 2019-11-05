"""""
--------------------------------------------------------------------------------------------------------
    A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
--------------------------------------------------------------------------------------------------------
"""
# importing the numpy for using the 2D arrays
from numpy import *
class Array:
    def printing(self):
        # taking no of rows and no of coloumns
        r = int(input("Enter the numbers of rows "))
        c = int(input("Enter the numbers, of coloumns "))
        length = r*c
        arr = []
        print("Enter elements elements into array ")
        # taking integer elemnts from the user
        for i in range(1, length+1):
            var = int(input("Enter INT ele : "))
            arr.append(var)
        integer = array(arr)
        # changing the array into 2D array and printing the 2D integer array
        integer = integer.reshape(3, 3)
        arr.clear()
        for i in range(1, length+1):
            # taking float elements to the array
            var = float(input("Enter float ele : "))
            arr.append(var)
        Float = array(arr)
        # changing the array into 2D array and printing the 2D float array
        Float = Float.reshape(3, 3)
        arr.clear()
        for i in range(1, length + 1):
            var = bool(input("Enter Boolean ele : "))
            arr.append(var)
        Boolean = array(arr)
        # changing the array into 2D array and printing the 2D boolean array
        Boolean = Boolean.reshape(3, 3)
        count = 0
        print(" INTEGER ARRAY >>>  ")
        print(integer)
        print(" FLOAT ARRAY >>>")
        print(Float)
        print(" BOOLEAN ARRAY >>> ")
        print(Boolean)
ob = Array()
ob.printing()