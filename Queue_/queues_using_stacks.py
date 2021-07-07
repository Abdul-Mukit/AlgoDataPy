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

    def __str__(self):
        return str(self.__dict__)

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
            self.length -= 1
            return temp

    def peek(self):
        return self.top

    def print_list(self):
        cur_node = self.top
        stack_values = []
        while cur_node is not None:
            stack_values.append(cur_node.value)
            cur_node = cur_node.next
        print(stack_values)


# # Demonstration of reversing stack
# stack = Stack()
# reverse_stack = Stack()
#
# stack.push(0)
# stack.push(1)
# stack.push(2)
#
# print("Stack:")
# stack.print_list()
# print("Reverse Stack:")
# reverse_stack.print_list()
#
# for i in range(stack.length):
#     reverse_stack.push(stack.pop().value)
#
# print("Stack:")
# stack.print_list()
# print("Reverse Stack:")
# reverse_stack.print_list()


class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.reverse_stack = Stack()

    def enqueue(self, value):
        for i in range(self.reverse_stack.length): # reconstruct stack to push
            self.stack.push(self.reverse_stack.pop().value)
        self.stack.push(value)

    def dequeue(self):
        for i in range(self.stack.length): # reconstruct reverse_stack to pop but have FIFO appearance
            self.reverse_stack.push(self.stack.pop().value)
        return self.reverse_stack.pop()


    def peek(self):
        if self.stack.length == 0:
            return self.reverse_stack.top
        elif self.reverse_stack.length == 0:
            return self.stack.bottom

    def print_list(self):
        for i in range(self.stack.length): # reconstruct reverse_stack to print
            self.reverse_stack.push(self.stack.pop().value)
        self.reverse_stack.print_list()

# Testing the new
my_queue = MyQueue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)


popped = my_queue.dequeue()
print("Dequeued: {}".format(popped.value))
print("New first: {}".format(my_queue.peek()))

popped = my_queue.dequeue()
print("Dequeued: {}".format(popped.value))
print("New first: {}".format(my_queue.peek()))

popped = my_queue.dequeue()
print("Dequeued: {}".format(popped.value))
print("New first: {}".format(my_queue.peek()))

my_queue.print_list()


