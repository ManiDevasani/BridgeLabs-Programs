"""""
-----------------------------------------------------------------------------------------------------------
1. Read .a List of Numbers from a file and arrange it ascending Order in a
Linked List. Take user input for a number, if found then pop the number out of the
list else insert the number in appropriate position
-----------------------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.LinkedList import LinkedList


class UnordredList:
    if __name__ == '__main__':
        # Creating the object of the linked list
        List = LinkedList()
        # opening the file in read mode and spliting it using the words String
        file = open("manitxt", "r")
        for i in file:
            words = i.split(" ")
        # After spliting adding the elements to the list
        for i in words:
            List.add(i)
        #     taking the input string from the user to search weather it is present in the list or not
        String = str(input("Enter the String to check : "))
        print("Before Searching elements in the list are : ")
        # printing the list before searching
        List.show()
        # calling the searching method in the linked list class passing the string
        # if the element is present in the list then it will delete element from the list
        if List.search(String):
            index = List.indexOf(String)
            List.pop(String)
            print("After searching elements in the list are : ")
            List.show()
            print("Element removed at :", index)
        # if the string is not present in the list it will be added to the list
        else:
            List.add(String)
            print("After searching")
            # After adding to the list printing list
            List.show()
            print("Element added at Last of the list ")
            # open the file in a+ mode it means for adding the text to the file
            # here we are adding the string to the file and after adding closing the file
            f = open("manitxt", "a+")
            f.write(String)
            f.close()
