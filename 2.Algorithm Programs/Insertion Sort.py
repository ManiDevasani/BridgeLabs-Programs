"""""
-----------------------------------------------------------------------------
1. Reads in strings from standard input and prints them in sorted order.
Uses insertion sort.
-----------------------------------------------------------------------------
"""


class InsertionSort:
    @staticmethod
    def sorting():
        arr = []
        n = int(input("Enter the number of strings to be entered : "))
        # Inserting the elements into the array
        for i in range(0, n):
            list.append(input("Enter String : "))
        # constant increment of i values
        for i in range(0, len(arr)):
            j = i+1
            # Every time j starts from 0 to len of list and moves the lower element to left side by swapping
            # Every time it traverse to last of the list
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        # Printing the swapping list
        print(list)


InsertionSort.sorting()


