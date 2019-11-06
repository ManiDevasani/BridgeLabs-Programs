"""""
----------------------------------------------------------------------------------------------------------
1. Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack using
the Linked List and Print the Anagrams in the Reverse Order. Note no Collection
Library can be used.
----------------------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Stack import Stack


class AnagramStack:
    @staticmethod
    def inserting():
        # creating the stacks objects and named it as 's' and 's1'
        # 's' for prime number s from 0 to 1000
        # 's1' for anagrams between 0 to 1000
        s = Stack()
        s1 = Stack()
        # Taking range from 0 to 1000
        for i in range(2, 1000):
            count = 0
            # if count is incremented then that number is not a prime number
            for num in range(2, (i // 2 + 1)):
                if i % num == 0:
                    count += 1
            # if the count is not equal to zero then it will add to the queue 's'
            if count == 0 and i != 1:
                s.push(i)
        # running the loop in the range of 's' size in reverse
        for i in range(s.size(), 0, -1):
            for j in range(i + 1, s.size()):
                # Every time it calls the anagram method and pass the element as 'i' element is constant
                # and 'j' value changes along with the values.
                # if the element is true then the numbers are added to the 's1' queue.
                if AnagramStack.anagram(s.get(i), s.get(j)):
                    s1.push(s.get(i))
                    s1.push(s.get(j))
        # Printing the anagram and prime numbers between 0 to 1000
        s.show()
        print()
        s1.show()

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


AnagramStack.inserting()
