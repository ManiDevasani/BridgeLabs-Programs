"""""
------------------------------------------------------------------------------------------------
a. Create Utility Class having following static methods
i. binarySearch method for integer
ii. binarySearch method for String
iii. insertionSort method for integer
iv. insertionSort method for String
v. bubbleSort method for integer
vi. bubbleSort method for String
b. Write main function to call the utility function
------------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Util import Util


class MainMethod:
    @staticmethod
    def method():
        # imported time class to calculate the elapsed time
        import time
        u = Util()
        # creating the integer array and string string
        intList = [2, 8, 6, 1, 4, 3, 9, 5, 7]
        StringList = ['m', 'a', 'n', 'i', 'k', 'a', 'n', 't', 'a']
        # starting time before calling binary search of integer method in util class
        start1 = time.time()
        u.binarysearchint(intList, 6)
        stop1 = time.time()
        # stop the time and calculate the difference between them and printing
        BinaryInt = stop1 - start1
        print("ELAPSED TIME FOR BINARY SEARCH OF INTEGER LIST  :", BinaryInt)
        # starting time before calling binary search of string method in util class
        start2 = time.time()
        u.binarySearchString(StringList, "t")
        stop2 = time.time()
        # stop the time and calculate the difference between them and printing
        BinaryStr = stop2 - start2
        print("ELAPSED TIME FOR BINARY SEARCH OF STRING LIST   :", BinaryStr)
        # starting time before calling insertion sort of integer method in util class
        start3 = time.time()
        u.insertionsortInt(intList)
        stop3 = time.time()
        # stop the time and calculate the difference between them and printing
        InserInt = stop3 - start3
        print("ELAPSED TIME FOR INSERTION SORT OF INTEGER LIST :", InserInt)
        # starting time before calling insertion sort of string method in util class
        start4 = time.time()
        u.insertionsortStr(StringList)
        stop4 = time.time()
        # stop the time and calculate the difference between them and printing
        InseStr = stop4 - start4
        print("ELAPSED TIME FOR INSERTION SORT OF STRING LIST  :", InseStr)
        # starting time before calling bubble sort of integer method in util class
        start5 = time.time()
        u.bubbleSortInt(intList)
        stop5 = time.time()
        # stop the time and calculate the difference between them and printing
        BubbleInt = stop5 - start5
        print("ELAPSED TIME FOR BUBBLE SORT OF INTEGER LIST    :", BubbleInt)
        # starting time before calling bubble sort of string method in util class
        start6 = time.time()
        u.bubbleSortStr(StringList)
        stop6 = time.time()
        # stop the time and calculate the difference between them and printing
        BubbleStr = stop6 - start6
        print("ELAPSED TIME FOR BUBBLE SORT OF STRING LIST     :", BubbleStr)


# calling the method


MainMethod.method()
