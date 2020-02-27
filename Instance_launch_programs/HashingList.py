from Node import *


class HashingList:
    def __init__(self, data=None):
        # taking 7 slots that is 7 empty nodes and insert these empty nodes into list
        node1 = Node()
        node2 = Node()
        node3 = Node()
        node4 = Node()
        node5 = Node()
        node6 = Node()
        node7 = Node()
        # inserting the empty nodes into the list
        self.node_array = [node1, node2, node3, node4, node5, node6, node7]

    def insert(self, data, index):
        n = Node()
        n.data = data
        n.next = None
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

    def display(self):
        # Display the data regarding to the remainder and the index of the node array
        # In the array taking the index and printing the nodes in that nodes are connected
        for i in range(len(self.node_array)):
            # taking the node at the index of the node  array
            temp = self.node_array[i]
            # checking the next none condition until that it prints the data  in the node
            if temp is not None:
                print("Column", i + 1, "values are =>  ", end="")
                # if slot has no data then t will print none
                if temp.next is None:
                    print("None", end="")
                # if node is not none then printing te data in  that node
                while temp is not None:
                    if temp.data is not None:
                        print(temp.data, ",", end="")
                    temp = temp.next
                print()

    def instance_type(self, row):
        Vcpu = 0
        Memory = 0
        for i in range(3):
            num = 0
            # taking the node at the index of the node  array
            if i is not 0:
                temp = self.node_array[i]
                # checking the next none condition until that it prints the data  in the node
                if temp is not None:
                    while temp is not None:
                        if temp.data is not None:
                            num = num + 1
                            if num == row:
                                if i is 1:
                                    Vcpu = temp.data
                                if i is 2:
                                    Memory = temp.data
                        temp = temp.next
        if Vcpu <= 1 and Memory <= 1:
            return "t2.micro"
        if Vcpu <= 1 and 2 >= Memory > 1:
            return "t2.small"
        if Vcpu <= 2 and 4 >= Memory > 2:
            return "t2.medium"
        if Vcpu <= 2 and 8 >= Memory > 4:
            return "t2.large"

    def Image_id(self, row):
        linux_ami = "ami-05695932c5299858a"
        ubuntu_ami = "ami-0620d12a9cf777c87"
        windows_ami = "ami-07545b3a1f4619f4b"
        Image_name = ""

        num = 0
        temp = self.node_array[0]
        # checking the next none condition until that it prints the data  in the node
        if temp is not None:
            while temp is not None:
                if temp.data is not None:
                    num = num + 1
                    if num == row:
                        Image_name = str(temp.data)
                temp = temp.next
        if Image_name == 'ubuntu':
            return ubuntu_ami
        elif Image_name == 'linux':
            return linux_ami
        elif Image_name == 'windows':
            return windows_ami

    def min_count(self, row):
        count = 0
        num = 0
        temp = self.node_array[4]
        # checking the next none condition until that it prints the data  in the node
        if temp is not None:
            while temp is not None:
                if temp.data is not None:
                    num = num + 1
                    if num == row:
                        count = temp.data
                temp = temp.next
        return count

    def max_count(self, row):
        count = 0
        num = 0
        temp = self.node_array[5]
        # checking the next none condition until that it prints the data  in the node
        if temp is not None:
            while temp is not None:
                if temp.data is not None:
                    num = num + 1
                    if num == row:
                        count = temp.data
                temp = temp.next
        return count

    def storage(self, row):
        size = 0
        num = 0
        temp = self.node_array[3]
        # checking the next none condition until that it prints the data  in the node
        if temp is not None:
            while temp is not None:
                if temp.data is not None:
                    num = num + 1
                    if num == row:
                        size = temp.data
                temp = temp.next
        return size

    def Conformation(self, row):
        message = 0
        num = 0
        temp = self.node_array[6]
        # checking the next none condition until that it prints the data  in the node
        # if temp is not None:
        while temp.next is not None and temp is not None:
            if temp.next is not None:
                num = num + 1
                if num == row:
                    message = temp.next.data
            temp = temp.next
        return message
