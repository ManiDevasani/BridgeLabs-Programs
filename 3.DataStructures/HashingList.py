"""""
---------------------------------------------------------------------------------------------
1. Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
efficiently search a number from a given set of number
--> Using Node array.
@author : Manikanta Devasani
Date    : 11/9/2019
---------------------------------------------------------------------------------------------
"""


class Node:
    # creating the node class and defining the data and next as none.
    def __init__(self):
        self.data = None
        self.next = None


class HashingList:
    def __init__(self):
        # taking 11 slots that is 11 empty nodes and insert these empty nodes into list
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node5 = Node()
        node6 = Node()
        node7 = Node()
        node8 = Node()
        node9 = Node()
        node10 = Node()
        node11 = Node()
        # inserting the empty nodes into the list
        self.node_array = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11]

    def insert(self, data):
        # creating the node and inserting the data and the referring the next oto none
        n = Node()
        n.data = data
        n.next = None
        # Dividing the given number by 11 and storing the number in index variable
        index = int(data % 11)
        # taking the array element in which the index number is placed
        node = self.node_array[index]
        # if the node in that index is none then adding the data to that node
        if node is None:
            node = n
        else:
            # else taking the temp variable as the node
            temp = node
            # traversing to the end and adding the new node to the existing node
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def diplay(self):
        # Display the data regarding to the remainder and the index of the node array
        # In the array taking the index and printing the nodes in that nodes are connected
        for i in range(len(self.node_array)):
            # taking the node at the index of the node  array
            temp = self.node_array[i]
            # checking the next none condition until that it prints the data  in the node
            if temp is not None:
                print("Remainder", i, "numbers are =>  ", end="")
                # if slot has no data then t will print none
                if temp.next is None:
                    print("None", end=" ")
                # if node is not none then printing te data in  that node
                while temp is not None:
                    if temp.data is not None:
                        print(temp.data, end=" ")
                    temp = temp.next
                print()


class HashingList:
    if __name__ == '__main__':
        # calling the main method and creating the object of the hashing
        HashMap = HashingList()

        HashMap.insert(77)
        HashMap.insert(44)
        HashMap.insert(55)
        HashMap.insert(26)
        HashMap.insert(93)
        HashMap.insert(17)
        HashMap.insert(31)
        HashMap.insert(20)
        HashMap.insert(54)
        HashMap.insert(88)
        HashMap.diplay()
