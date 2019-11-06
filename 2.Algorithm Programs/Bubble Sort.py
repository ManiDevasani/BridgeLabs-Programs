"""""
--------------------------------------------------------------------------------------
1. Reads in integers prints them in sorted order using Bubble Sort
--------------------------------------------------------------------------------------
"""
class Bubble_Sort:
    @staticmethod
    def sort():
        arr = []
        n = int(input("Enter the number of integers to be entered : "))
        # Taking inputs from the user into the list
        for i in range(0, n):
            arr.append(input("Enter next Integer : "))
        # the first loop stats from the length and it decrements the value
        # inner loop is used to compare the subsequent value each time
        #  and moves the element to right side using swapping
        for i in range(len(arr)-1,0,-1):
            for j in range(i):
                if(arr[j]>arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        # Printing the sorted array
        print(arr)
Bubble_Sort.sort()
