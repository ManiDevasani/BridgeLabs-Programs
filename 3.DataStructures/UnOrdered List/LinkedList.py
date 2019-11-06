"""""
----------------------------------------------------------------------------------
--> Linked list contains nodes, where as node contains two parts.
  1) for storing data.
  2) for storing the address of the next element.
--> If we add elements to the linked list it will add at last of the list.
--> we can delete the elements at particular index.
--> The first of the list is called as HEAD
----------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Node import Node


class LinkedList:
    # initiating the head as None
    def __init__(self):
        self.head = None
    # creating a method to add elements to the list

    def add(self, data):
        # creating a node which contains data and the next address as null.
        node = Node(data)
        node.data = data
        node.next = None
        # if the head node is null it means the list is empty so we add referring the element as head.
        if self.head == None:
            self.head = node
        # if list contains elements already and we have to add elements at the end of the list.
        else:
            n = self.head
            # Here traversing to end of the list and adding the node at the last of the node.
            while n.next != None:
                n = n.next
            n.next = node
    def addInorder(self,data):
        var = LinkedList.size()
        temp = self.head
        while temp.next!=None:
            if temp.data>data:


    def size(self):
        # TO ge the size of the list just take a variable and initializing it with 0
        # and traveling to the end of the list and after every node incrementing the value of the variable
        n = self.head
        x = 0
        while n.next != None:
            n = n.next
            x += 1
        x += 1
        return x

    def index(self, index):
        # For finding the data at the given index
        # if given index number is greater than the size then it is out of boundary
        lent = LinkedList.size(self)
        if index >= lent:
            return 'Out Of Boundary'
        # if given index number is less than the 0 then it is out of boundary
        elif index < 0:
            return 'Out Of Boundary'
        else:
            # taking the size of the list and a variable and each time traversing incrementing the variable
            # if the variable is equal to the index then it will print the data in that node
            n = self.head
            count = 0
            while n.next != None:
                if count == index:
                    return n.data
                    break
                n = n.next
                count += 1
            if count == (lent - 1):
                return n.data

    def indexOf(self, data):
        # Finding the index number of the particular data
        #  taking the loacal variable as 0 and compare the that variable to size every time
        # if the data at the index is eqal to the given data then return the variable value as index
        n = self.head
        count = 0
        lent = LinkedList.size(self)
        while n.next != None:
            if data == LinkedList.index(self, count):
                return count
                break
            n = n.next
            count += 1
        if data == n.data:
            return count

    def search(self, data):
        # Searching the node data at particular index
        # same as the above method
        # first deine the size and while traversing time compare to the size and return the count
        n = self.head
        count = 0
        lent = LinkedList.size(self)
        while n.next != None:
            if data == LinkedList.index(self, count):
                return True
                break
            n = n.next
            count += 1
        if data == n.data:
            return True
        else:
            return False

    def pop(self, data):
        # deleting the data from the list
        # Getting the index of the element by using the  index of method
        pos = int(LinkedList.indexOf(self, data))
        temp = self.head
        # if position is zero then refer head to the next element
        if pos == 0:
            self.head = temp.next
        else:
            # Using the index number traverse upto before of that element
            for i in range(0, pos - 1):
                temp = temp.next
            # Storing the address of the element in a local varible temp1
            # By referring the temp1.next the variable is removed from the list
            temp1 = temp.next
            temp.next = temp1.next

    def show(self):
        # By traversing from head to the end of the list
        # while traversing time printing the data at that node
        temp = self.head
        while temp.next != None:
            print(temp.data, end=",")
            temp = temp.next
        print(temp.data)
