"""""
--------------------------------------------------------------------------------------------------------------------
1.Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file.
--------------------------------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.LinkedList import LinkedList


class OrderderdList:
    if __name__ == '__main__':
        # Creating the object of the linked list
        ListNum = LinkedList()
        # creating an empty array and importing the file and spliting it and adding to the array
        array = []
        file = open("maninums", "r")
        for i in file:
            nums = i.split()
        for i in nums:
            array.append(i)
        # After adding the elements into array adding the elements to the linked list
        array.sort()
        for i in array:
            ListNum.add(i)
        # printing the list before searching
        ListNum.show()
        # Taking the integer input from the user for searching
        num = int(input("Enter the value for searching : "))
        # calling the searching method in the linked list class passing the int value
        # if the element is present in the list then it will delete element from the list
        if ListNum.search(num):
            index = ListNum.indexOf(num)
            ListNum.pop(num)
            print("After searching elements in the list are : ")
            ListNum.show()
            print("Element removed at :", index)
        # else it will add to the list at the particular position
        else:
            # calling insertOrder method to insert element at particular position
            ListNum.insertOrder(num)
            print("After searching")
            ListNum.show()
            print("Element added at Last of the list ")
            # After adding the element into the list updating the file using the num string
            # num string will append all the elements in the list and finally add the string to the fila
            num = ""
            for i in range(ListNum.size()):
                var = str(ListNum.index(i))
                space = " "
                num = num + var + space
            print(num)
            # open the file in a+ mode it means for adding the text to the file
            # here we are adding the num string to the file and after adding closing the file
            f = open("maninums", "a+")
            f.write(num)
            f.close()
