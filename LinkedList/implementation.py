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
        new_node = Node(value=value)
        new_node.next = previous_node.next
        previous_node.next = new_node
        self.length += 1
        return

    # def remove(self, index):
    #     previsou_node = self.at(index-1)
    #     previsou_node.next = previsou_node.next.next


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.__dict__)


my_linked_list = LinkedList(0)
my_linked_list.append(1)
print(my_linked_list)
result = my_linked_list.at(1)
print("hello")