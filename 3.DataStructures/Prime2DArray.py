"""""
---------------------------------------------------------------------------------------------------
1. Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. Store
the prime numbers in a 2D Array, the first dimension represents the range 0-100,
100-200, and so on. While the second dimension represents the prime numbers in
that range
---------------------------------------------------------------------------------------------------
"""
from numpy import *


class TwoDmprime:
    @staticmethod
    def primeArray():
        # taking an empty list
        arr = []
        primelist = []
        anagram = []
        n = 0
        print("Print Numbers are : ")
        # For printing the prime numbers in separate arrays of the ranges
        for i in range(2, 1000):
            count = 0
            # if count is incremented then that number is not a prime number
            for num in range(2, i // 2 + 1):
                if i % num == 0:
                    count += 1
            # if the count is not equal to zero then it will add to the queue 'arr' and 'primelist'
            if count == 0 and i != 1:
                arr.append(i)
                primelist.append(i)
            # Printing the prime number from 0-100 in an array
            # after printing clearing the array
            if n == 98:
                print(arr)
                arr.clear()
            # Printing the prime number from 100-200 in an array
            # after printing clearing the array
            if n == 198:
                print(arr)
                arr.clear()
            # Printing the prime number from 200-300 in an array
            # after printing clearing the array
            if n == 298:
                print(arr)
                arr.clear()
            # Printing the prime number from 300-400 in an array
            # after printing clearing the array
            if n == 398:
                print(arr)
                arr.clear()
            # Printing the prime number from 400-500 in an array
            # after printing clearing the array
            if n == 500:
                print(arr)
                arr.clear()
            # Printing the prime number from 500-600 in an array
            # after printing clearing the array
            if n == 598:
                print(arr)
                arr.clear()
            # Printing the prime number from 600-700 in an array
            # after printing clearing the array
            if n == 698:
                print(arr)
                arr.clear()
            # Printing the prime number from 700-800 in an array
            # after printing clearing the array
            if n == 798:
                print(arr)
                arr.clear()
            # Printing the prime number from 800-900 in an array
            # after printing clearing the array
            if n == 898:
                print(arr)
                arr.clear()
            # Printing the prime number from 900-100 in an array
            # after printing clearing the array
            if n == 997:
                print(arr)
                arr.clear()
            n += 1
        # running the loop in the range of 'primelist' size
        for i in range(0, len(primelist)):
            for j in range(i + 1, len(primelist)):
                # Every time it calls the anagram method and pass the element as 'i' element is constant
                # and 'j' value changes along with the values.
                # if the element is true then the numbers are added to the 'anagram' list.
                if TwoDmprime.anagram(primelist[i], primelist[j]):
                    anagram.append(primelist[i])
                    anagram.append(primelist[j])
        anagram = array(anagram)
        # changing anagram array into 2d array
        anagram = anagram.reshape(79, 2)
        # Printing the anagrams
        print("Anagrams are : ")
        print(anagram)

    @staticmethod
    def anagram(a, b):
        import math
        # Taking two empty arrays for checking the equals condition.
        a1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        temp1 = a
        # this while loop is increment the values in array a1
        while temp1 != 0:
            r = math.floor(temp1 % 10)
            a1[r] += 1
            temp1 = math.floor(temp1 / 10)
        temp2 = b
        # this loop increment the values in array a2
        while temp2 != 0:
            r = math.floor(temp2 % 10)
            a2[r] += 1
            temp2 = math.floor(temp2 / 10)
        # if both arrays are equals then the given strings are  anagram
        if a1 == a2:
            return True
        else:
            return False


TwoDmprime.primeArray()
