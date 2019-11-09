"""""
-------------------------------------------------------------------------------------------
Circular Linked List:
--> It is same as linked list, but in linked list last element is null.
--> But in circular linked list the last element is referred to the head of the  list.
--> Hence the resultant will be circular linked list.

@author : Manikanta Devasani
Date   : 11/9/2019
-------------------------------------------------------------------------------------------
"""


class Node:
    # Taking the class node and initialising the data and next variables
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularList:
    # creating the circular list list class and initializing the head and last as null
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        # inserting the data at the last of the list and referring the last to the head of the list
        # creating a node and inserting the data and next as null
        node = Node(data)
        node.data = data
        node.next = None
        # if head and last is none it means the list is empty.
        # if list is empty then adding the node to the list and referring the head and last as that node.
        if self.head is None:
            self.head = self.last = node
            self.last.next = self.head
        else:
            # else the new node is added at the last of the node and the last node is changed to the new node.
            self.last.next = node
            node.next = self.head
            self.last = node

    def show(self):
        # Printing the list from head to last
        # Taking the temporary variable as head and traversing from head to last
        # And printing the data at each node
        temp = self.head
        temp1 = self.last
        while temp is not None:
            print(temp.data, end=" ")
            # if head is equals to last the loop breaks it means it is the last position
            if temp == temp1:
                break
            temp = temp.next

    def size(self):
        # taking the count variable as 0
        # Taking the temporary variable as head and traversing from head to last
        # And printing the data at each node
        count = int(0)
        temp = self.head
        temp1 = self.last
        while temp is not None:
            count += 1
            # if head is equals to last the loop breaks it means it is the last position
            if temp == temp1:
                break
            temp = temp.next
        return count

    def insertAt(self, index, data):
        # To insert the node at the particular position in the list
        # creating the node and initialising the data and the next as none
        node = Node(data)
        node.data = data
        node.next = None
        temp = self.head
        # traversing to the position before the index and changing the address of the node to the new node
        # And connect the new node to the list
        for i in range(index - 1):
            temp = temp.next
        # Storing the address of the current node in 'a' and after adding the new node to the list and connect 'a'
        a = temp.next
        temp.next = node
        node.next = a

    def delete(self, index):
        # deleting the node from the list
        # Taking the temporary variable and refer to head
        temp = self.head
        # if the given index is 0 then deleting the first element
        if index == 0:
            self.head = temp.next
        # if the index is equal to the size of the element then remove the last node
        # By taking the size of the list and traversing to the last node and deleting the node
        elif index == int(CircularList.size(self) - 1):
            s = int(CircularList.size(self)) - 1
            for i in range(s - 1):
                temp = temp.next
            temp.next = self.head
            self.last = temp
        else:
            # traverse upto the before index number and remove the node from the list
            for i in range(index - 1):
                temp = temp.next
            a1 = temp.next
            temp.next = a1.next


class Main:
    if __name__ == '__main__':
        d = CircularList()
        n = int(input("Enter no of numbers to insert : "))
        for i in range(n):
            d.insert(int(input("Enter element : ")))
        print("After entering the elements in to the list ")
        d.show()
        print()
        n1 = int(input("Enter the index number to delete : "))
        d.delete(n1)
        print("After deleting the element from the list ")
        d.show()
        print()
        index = int(input("Enter the index number to insert the element :"))
        data = int(input("Enter the data to insert the list :"))
        print("After entering the element in to the list ")
        d.insertAt(index, data)
        d.show()
        size = d.size()
        print()
        print("size of the list : ", size)
