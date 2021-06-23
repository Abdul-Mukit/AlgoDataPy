class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        new_node = Node(value, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def at(self, index):
        cur_node = self.head
        i = 0
        while cur_node is not None:
            if i == index:
                break
            else:
                cur_node = cur_node.next
                i += 1

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
        elif index >= self.length:
            self.append(value)
            return

        previous_node = self.at(index-1)
        next_node = previous_node.next
        new_node = Node(value=value, next=next_node, prev=previous_node)
        previous_node.next = new_node
        next_node.prev = new_node
        self.length += 1
        return

    def remove(self, index):
        if index >= self.length:
            print("Warning: index out of bounds")
            return
        elif index == 0:
            self.head = self.head.next
        elif index == self.length-1:
            previous_node = self.at(index-1)
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node = self.at(index-1)
            previous_node.next = previous_node.next.next

        self.length -= 1


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.__dict__)

my_list = DoublyLinkedList(0)
my_list.__str__()
my_list.prepend(-1)
my_list.prepend(-2)
my_list.at(0)
my_list.__str__()