class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        return_val = True

        if self.root is None:
            self.root = Node(value)
        else:
            cur_node = self.root
            while cur_node is not None:  # Traverse Tree
                if value < cur_node.value:  # go left?
                    if cur_node.left is None:
                        cur_node.left = Node(value)
                        break
                    else:
                        cur_node = cur_node.left
                elif value > cur_node.value:  # go right?
                    if cur_node.right is None:
                        cur_node.right = Node(value)
                        break
                    else:
                        cur_node = cur_node.right
                else:  # same value entered?`
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

        return None  # list traversing completed, entry not found

def traverse(cur_node: Node):
    if cur_node is None:  # based condition
        return str(None)
    else:  # recursive condition
        left_str = traverse(cur_node.left)
        right_str = traverse(cur_node.right)
        ret_str = "{}({},{})".format(cur_node.value, left_str, right_str)
        return ret_str


def bfs(tree: BinarySearchTree) -> []:
    current_node = tree.root
    output_list = []
    level_queue = []

    level_queue.append(current_node)

    while len(level_queue) != 0:
        current_node = level_queue.pop(0)
        output_list.append(current_node.value)

        if current_node.left is not None:
            level_queue.append(current_node.left)

        if current_node.right is not None:
            level_queue.append(current_node.right)

    return output_list


def traverse_inorder(node: Node, output_list: list) -> []:
    if node.left:
        output_list = traverse_inorder(node.left, output_list)

    output_list.append(node.value)

    if node.right:
        output_list = traverse_inorder(node.right, output_list)

    return output_list


def traverse_preorder(node: Node, output_list: list) -> []:
    output_list.append(node.value)
    if node.left:
        output_list = traverse_preorder(node.left, output_list)

    if node.right:
        output_list = traverse_preorder(node.right, output_list)

    return output_list


def traverse_postorder(node: Node, output_list: list) -> []:
    if node.left:
        output_list = traverse_postorder(node.left, output_list)

    if node.right:
        output_list = traverse_postorder(node.right, output_list)

    output_list.append(node.value)

    return output_list


def dfs_inroder(tree: BinarySearchTree):
    output_list = []
    output_list = traverse_inorder(tree.root, output_list)
    print(output_list)


def dfs_preorder(tree: BinarySearchTree):
    output_list = []
    output_list = traverse_preorder(tree.root, output_list)
    print(output_list)

def dfs_postorder(tree: BinarySearchTree):
    output_list = []
    output_list = traverse_postorder(tree.root, output_list)
    print(output_list)


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

print(traverse(myTree.root))
dfs_postorder(myTree)




