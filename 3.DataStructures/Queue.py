"""""
-------------------------------------------------------------------------------------------------
--> queue means it will add the elements at rear and removes the first element
--> it follows FIFO First In Last Out
--> it consists front ad rear
    1. front --> front of the queue
    2.rear --> last of the queue
--> enqueue adds the element at the rear
--> deque remove the element at first
-------------------------------------------------------------------------------------------------
"""
from Scripts.com.BridgeLabs.Functional.Node import Node


class Queue:
    # creating the variables front and rear and a count variable
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, data):
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
        # if the front element is none means there is no element in the queue then the list is empty
        if self.front is None:
            return True
        else:
            return False

    def size(self):
        # returns the count value if it is not equals to 0
        if self.count < 0:
            print("Out of index")
        # else returning the count
        else:
            return self.count

    def dequeue(self):
        # if the queue is empty then it will prints the below context
        if Queue.isEmpty(self):
            return " Queue is Empty "
        # front will assigned to the next to the front element and assigning that element as front of the queue
        else:
            if self.front.next is None:
                self.front = None
            self.front = self.front.next
            self.count -= 1

    def get(self, index):
        # Getting the data at particular index
        # if the size is less or greater than zero  then queue is empty
        lent = Queue.size(self)
        if index >= lent:
            return 'Out Of Boundary'
        elif index < 0:
            return 'Out Of Boundary'
        else:
            # else it will traverse and check the data at each point if it will equals then it will exit from the loop
            n = self.front
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
        temp = self.front
        if temp is None:
            print(None)
        else:
            while temp.next is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print(temp.data)
