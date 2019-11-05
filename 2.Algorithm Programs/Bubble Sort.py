"""""
--------------------------------------------------------------------------------------
1. Reads in integers prints them in sorted order using Bubble Sort
--------------------------------------------------------------------------------------
"""
class BubbleSort:
    def sort(self):
        List = []
        n = int(input("Enter the number of integers to be entered : "))
        # Taking inputs from the user into the list
        for i in range(0, n):
            List.append(input("Enter next Integer : "))
        # the first loop stats from the length and it decrements the value
        # inner loop is used to compare the subsequent value each time
        #  and moves the element to right side using swapping
        for i in range(len(List)-1,0,-1):
            for j in range(i):
                if(List[j]>List[j+1]):
                    temp = List[j]
                    List[j] = List[j+1]
                    List[j+1] = temp
        # Printing the sorted array
        print(List)
sorting = BubbleSort()
sorting.sort()