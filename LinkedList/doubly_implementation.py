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
        traverse = 0 if (index < int((self.length-1)/2)) else 1
        print(traverse)
        traverse_forward = 0
        traverse_reverse = 1

        if traverse == traverse_forward:
            i = 0
            cur_node = self.head
        elif traverse == traverse_reverse:
            i = self.length-1
            cur_node = self.tail

        while cur_node is not None:
            if i == index:
                break
            elif traverse == traverse_forward:
                cur_node = cur_node.next
                i += 1
            elif traverse == traverse_reverse:
                cur_node = cur_node.prev
                i -= 1

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

        elif index >= self.length:
            self.append(value)
        else:
            previous_node = self.at(index-1)
            next_node = previous_node.next
            new_node = Node(value=value, next=next_node, prev=previous_node)
            previous_node.next = new_node
            next_node.prev = new_node
            self.length += 1

    def remove(self, index):
        if index >= self.length:
            print("Warning: index out of bounds")
            return
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length-1:
            self.tail = self.tail.prev # this was not possible in singly
            self.tail.next = None
        else:
            previous_node = self.at(index-1)
            next_node = previous_node.next.next
            previous_node.next = next_node
            next_node.prev = previous_node

        self.length -= 1


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.__dict__)

my_list = DoublyLinkedList(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

print(my_list)
print(my_list.at(0))
print(my_list.at(1))
print(my_list.at(2))
print(my_list.at(3))
print(my_list.at(4))
