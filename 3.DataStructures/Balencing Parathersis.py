"""""
-----------------------------------------------------------------------------------
1. Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.
-----------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Stack import Stack


class BalencingParathersis:
    if __name__ == '__main__':
        # taking the expression in the form of String
        String = str(input("Enter the Expression : "))
        # creating the stack object
        s = Stack()
        length = len(String)
        # running the loop in the range of length of String
        # And taking each character
        for i in range(length):
            c = String[i]
            # if the character c is equals to '(' then it will push to the stack else it will continue the loop
            if c == "(":
                s.push("(")
            # if the character c is equals to ')' then it will pop the data from the queue
            elif c == ")":
                s.pop()
        # After the loop finished then the checking the stack is epty or not
        check = s.isEmpty()
        # if the stack is empty then the given expression is balanced
        if check:
            print("True Expression is Balanced ")
        # else the given expression is balanced
        else:
            print("False expression is not balanced")
