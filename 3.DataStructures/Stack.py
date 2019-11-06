"""""
-------------------------------------------------------------------------------------------------
--> stack means it will add the elements one on another
--> it follows LIFO Last In First Out
--> it consists top element
--> stack adds the element at top
--> stack removes the top element
--> peek()-> prints the top element
-------------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Node import Node


class Stack:
    # creating the variables top and a count variable
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        # inserting the element at the top
        # creating the node object and passing the given data to it and assigning the given data to it.
        node = Node(data)
        node.data = data
        node.next = None
        # if in top there are no elements then given data will be assigned as top
        if self.top is None:
            self.top = node
            self.count += 1
        # else the next of the top element is assigned as node and the  top is assigned as node
        else:
            node.next = self.top
            self.top = node
            self.count += 1

    def pop(self):
        # removes the top element
        # if stack is empty it will prints the below context
        if Stack.isEmpty(self):
            print("Out of Boundary")
        # if there is only one element is present in the list then it will be assigned as None
        elif self.top.next is None:
            self.top = None
            self.count -= 1
        # else if top is assigned to the next of the top element
        else:
            self.top = self.top.next
            self.count -= 1

    def isEmpty(self):
        # returns weather the stack is empty or not
        if self.top is not None:
            return True
        else:
            return False

    def peek(self):
        # Prints the top element
        print(self.top.data)

    def size(self):
        # returns the count value if it is not equals to 0
        if self.count < 0:
            print("Out of index")
        # else returning the count
        else:
            return self.count

    def get(self, index):
        # Getting the data at particular index
        # if the size is less or greater than zero  then stack is empty
        lent = Stack.size(self)
        if index >= lent:
            return 'Out Of Boundary'
        elif index < 0:
            return 'Out Of Boundary'
        # else it will traverse and check the data at each point if it will equals then it will exit from the loop
        else:
            n = self.top
            count = 0
            while n.next is not None:
                if count == index:
                    return n.data
                    break
                n = n.next
                count += 1
            if count == (lent - 1):
                return n.data

    def show(self):
        # traversing from front element to the last element
        # printing the data at each node
        temp = self.top
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
