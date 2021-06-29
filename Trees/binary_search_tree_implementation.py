class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        return_val = True

        if self.root is None:
            self.root = Node(value)
        else:
            cur_node = self.root
            while cur_node is not None: # Traverse Tree
                if value < cur_node.value: # go left?
                    if cur_node.left is None:
                        cur_node.left = Node(value)
                        break
                    else:
                        cur_node = cur_node.left
                elif value > cur_node.value: # go right?
                    if cur_node.right is None:
                        cur_node.right = Node(value)
                        break
                    else:
                        cur_node = cur_node.right
                else: # same value entered?`
                    return_val = False
                    print("Can't input value that already exists")
        return return_val

    def lookup(self, value):
        cur_node = self.root
        while cur_node is not None:
            if cur_node.value == value:
                return cur_node
            elif value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right

        return None # list traversing completed, entry not found


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

print("Found: {}".format(myTree.lookup(9)))
print("Found: {}".format(myTree.lookup(20)))
print("Found: {}".format(myTree.lookup(15)))
print("Found: {}".format(myTree.lookup(133)))
