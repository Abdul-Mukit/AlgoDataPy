# My comments:
# This is a linked list in the format:
# top -> ... -> bottom
# Push is LinkedList.prepend()
# Pop is LinkedList.remove(0) which is an 0(1). If push was append and list was: bottom -> ... -> top then pop would be
# O(n) for singly linked list

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.__dict__)

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value): # or prepend of linked list.
        if self.length == 0:
            self.bottom = self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def at(self, index):
        cur_node = self.top
        i = 0
        while cur_node is not None:
            if i == index:
                break
            else:
                cur_node = cur_node.next
                i += 1
        return cur_node

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.bottom
            self.top = self.bottom = None
            self.length -= 1
            return temp
        elif self.length > 1:
            temp = self.top
            self.top = self.top.next
            return temp

    def peak(self):
        return self.top

    def print_list(self):
        cur_node = self.top
        stack_values = []
        while cur_node is not None:
            stack_values.append(cur_node.value)
            cur_node = cur_node.next
        print(stack_values)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_list()

popped = my_stack.pop()
print("Popped: {}".format(popped.value))
print("New top: {}".format(my_stack.peak()))

popped = my_stack.pop()
print("Popped: {}".format(popped.value))
print("New top: {}".format(my_stack.peak()))

popped = my_stack.pop()
print("Popped: {}".format(popped.value))
print("New top: {}".format(my_stack.peak()))

my_stack.print_list()