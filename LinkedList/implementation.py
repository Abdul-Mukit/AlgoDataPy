# 10 > 5 > 16

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def at(self, index):
        cur_node = self.head

        for i in range(index):
            if cur_node.next is not None:
                cur_node = cur_node.next
                print("Accessed {} th element".format(i+1))
            else:
                print("Error: the index {} element not found".format(index))
                return None
        return cur_node

    def print_list(self):
        array = []
        cur_node = self.head
        while cur_node is not None:
            array.append(cur_node.value)
            cur_node = cur_node.next
        print(array)

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return

        cur_node = self.head
        new_node = Node(value=value)
        i = 0
        while cur_node is not None:
            if i+1 == index:
                new_node.next = cur_node.next
                cur_node.next = new_node
                self.length += 1
                return
            else:
                cur_node = cur_node.next
                i += 1

        print("Selected index not available for insert operation")
        return




class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.__dict__)


my_linked_list = LinkedList(0)
my_linked_list.append(2)
print(my_linked_list)