class SinglyLinkedList:
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
        elif index >= self.length:
            self.append(value)
        else:
            previous_node = self.at(index-1)
            new_node = Node(value=value)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.length += 1

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

    def reverse(self):
        cur_node = self.head
        prev_node = None

        while cur_node is not None:
            next_node = cur_node.next # keep reference to not loose
            cur_node.next = prev_node # main pointer reversing job
            # now increment pointer
            prev_node = cur_node
            cur_node = next_node

        self.tail = self.head
        self.head = prev_node # last prev_Node would be the original tail node


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.__dict__)


# testing code
my_list = SinglyLinkedList(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()
print(my_list)


my_list.reverse()
my_list.print_list()
print(my_list)

