"""""
-----------------------------------------------------------------------------
1. Reads in strings from standard input and prints them in sorted order.
Uses insertion sort.
-----------------------------------------------------------------------------
"""
class InsertionSort:
    def sorting(self):
        list =[]
        n = int(input("Enter the number of strings to be entered : "))
        # INserting the elements into the array
        for i in range(0, n):
            list.append(int(input("Enter String : ")))
        # constant increment of i values
        for i in range(0,len(list)):
            j = i+1
            # Every time j starts from 0 to len of list and moves the lower element to left side by swapping
            # Every time it traverse to last of the list
            for j in range(len(list)):
                if (list[i]<list[j]):
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        # Printing the swapping list
        print(list)
insert = InsertionSort()
insert.sorting()


