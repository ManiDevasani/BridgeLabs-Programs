"""""
-----------------------------------------------------------------------------------------------
1. A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.
-----------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Dequeue import Dequeue


class PolindromeChecker:
    if __name__ == '__main__':
        print("Enter the String : ")
        # creating the Dequeue object
        q = Dequeue()
        String = input()
        length = len(String)
        # Taking the string as input for checking the palindrome condition
        # taking the string length and inserting each element in the dequeue
        for i in String:
            q.insertRear(i)
        size = q.size()
        # Taking the new string and adding the characters to it
        # By removing reversely from the queue
        newstr = ""
        for i in range(0, size):
            s = q.removeRear()
            newstr += s
        # if the given string is equal to the reversed string then it is a palindrome else it is not
        if String == newstr:
            print("---Given String is Palindrome---")
        else:
            print("---Given String is NOT Palindrome---")
