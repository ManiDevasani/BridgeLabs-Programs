"""""
----------------------------------------------
1.BINARY SEARCH TREE
----------------------------------------------
"""
class node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None
class BSTree:
        # initializing the root node
        def __init__(self):
            self.root = None
        # inserting the data to the nodes in sorting order
        def insert(self,data):
            # if root is none then the data is assigned to the rot node
            if self.root==None:
                self.root = node(data)
            # else it calls the insert method recursively to arrange in sorting order
            else:
                self._insert(data,self.root)
        def _insert(self,data,cur_node):
            # if the data is less than the current node data then it will assigned to left child
            if data<cur_node.data:
                # if left child is null then the data is assigned to left child
                if cur_node.left_child==None:
                    cur_node.left_child = node(data)
                # else it calls recursively the insert method to arrange in sorting order
                else:
                    self._insert(data,cur_node.left_child)
            # if the data is greater than the current node data then it will assigned to right child
            elif data>cur_node.data:
                # if right child is null then the data is assigned to right child
                if cur_node.right_child==None:
                    cur_node.right_child = node(data)
                # else it calls recursively the insert method to arrange in sorting order
                else:
                    self._insert(data,cur_node.right_child)
            # not accesing the repeatig data in the tree
            else:
                print("Dupilicates are not allowed")
        # displaying the elements in the tree
        def show(self):
            # if root is not null then recursively calling the print method for printing
            if self.root!=None:
                self._print(self.root)
        def _print(self,cur_node):
            # printing the values in sorting order
            if cur_node!=None:
                 self._print(cur_node.left_child)
                 print (str(cur_node.data))
                 self._print(cur_node.right_child)
tree = BSTree()
tree.insert(4)
tree.insert(4)
tree.insert(3)
tree.insert(27)
tree.insert(2)
tree.insert(1)
tree.show()


