# My comments:
# This is a linked list in the format:
# first -> ... -> last
# Push is LinkedList.append()
# In this configuration, push() and Pop() both are O(1)
# Pop() would not have been O1 if list was: last -> ... -> first and push was prepend().
# that is because I would have to traverse n times in singly linked list to pop the first value


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)


class Stack:
    def __init__(self):
        self.last = None
        self.first = None
        self.length = 0

    def enqueue(self, value): # or prepend of linked list.
        if self.length == 0:
            self.first = self.last = Node(value)
        else:  # append() with list orientation: first ->...-> last
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def at(self, index):
        cur_node = self.first
        i = 0
        while cur_node is not None:
            if i == index:
                break
            else:
                cur_node = cur_node.next
                i += 1
        return cur_node

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.first
            self.last = self.first = None
            self.length -= 1
            return temp
        elif self.length > 1:
            temp = self.first
            self.first = self.first.next
            return temp

    def peek(self): # look at first as it will be popped
        return self.first

    def print_list(self):
        cur_node = self.first
        stack_values = []
        while cur_node is not None:
            stack_values.append(cur_node.value)
            cur_node = cur_node.next
        print(stack_values)


my_stack = Stack()
my_stack.enqueue(1)
my_stack.enqueue(2)
my_stack.enqueue(3)

my_stack.print_list()

popped = my_stack.dequeue()
print("Dequeued: {}".format(popped.value))
print("New first: {}".format(my_stack.peek()))

popped = my_stack.dequeue()
print("Dequeued: {}".format(popped.value))
print("New first: {}".format(my_stack.peek()))

popped = my_stack.dequeue()
print("Dequeued: {}".format(popped.value))
print("New first: {}".format(my_stack.peek()))

my_stack.print_list()