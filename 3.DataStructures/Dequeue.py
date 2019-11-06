"""""
---------------------------------------------------------------------------------------
--> Deque means it will add the elements from front end or from last in queue
--> it consists front ad rear
    1. front --> front of the queue
    2.rear --> last of the queue
---------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Node import Node


class Dequeue:
    def __init__(self):
        # creating the variables front and rear and a count variable
        self.front = None
        self.rear = None
        self.count = 0

    def insertFront(self, data):
        # inserting the element from the front
        # creating the node object and passing the given data to it and assigning the given data to it.
        node = Node(data)
        node.data = data
        node.next = None
        # if the queue is empty it means front is none then the given data is the front data
        if self.front is None:
            self.front = self.rear = node
        # else given data will assigned to the next to the front and assigning the given node as front of the queue
        node.next = self.front
        self.front = node
        self.count += 1

    def insertRear(self, data):
        # Inserting the data at the last of the queue
        # creating the node object and passing the given data to it and assigning the given data to it.
        node = Node(data)
        node.data = data
        node.next = None
        # if the queue is empty it means front is none then the given data is the rear data
        if self.rear is None:
            self.front = self.rear = node
        # else given data will assigned to the next to the rear and assigning the given node as rear of the queue
        self.rear.next = node
        self.rear = node
        self.count += 1

    def isEmpty(self):
        # if the front element is none means there is noo element in the queue then the list is empty
        if self.front is None:
            return True
        else:
            return False

    def removeFront(self):
        # removing the front element in the queue
        #  if size is zero then queue is empty
        if Dequeue.size(self) == 0:
            return None
        # if the there are one element in the queue then deleting by referring it to the none
        else:
            if self.front.next is None:
                n = self.front.data
                self.front = None
                return n
            # removing the front data and assigning the next to the front element as the front
            else:
                n = self.front.data
                self.front = self.front.next
                self.count -= 1
                return n

    def removeRear(self):
        # removing the rear element in the queue
        #  if size is zero then queue is empty
        if Dequeue.size(self) == 0:
            return None
        else:
            # taking the size of the queue and traversing before to the last element
            #  And referring the last as None
            itr = Dequeue.size(self)
            temp = self.front
            for i in range(0, itr - 1):
                temp = temp.next
            n = temp.data
            temp = self.rear
            self.rear = temp
            self.count -= 1
            return n
            temp.data = None

    def size(self):
        # returns the count value if it is not equals to 0
        if self.count < 0:
            print("Out of index")
        # else returning the count
        else:
            return self.count

    def show(self):
        # traversing from front element to the last element
        # printing the data at each node
        temp = self.front
        itr = Dequeue.size(self)
        for i in range(0, itr):
            print(temp.data, end=" ")
            temp = temp.next
