# My comments:
# This is a array/list based implementation of stack. List in python already has append and pop method. So implementing
# very easy.


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value): # or prepend of linked list.
        self.stack_list.append(value)

    def pop(self):
        if self.length() > 0:
            return self.stack_list.pop()
        else:
            return None

    def peek(self):
        if self.length() > 0:
            return self.stack_list[-1]
        else:
            return None


    def print_list(self):
        print(self.stack_list)

    def length(self):
        return len(self.stack_list)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

my_stack.print_list()

popped = my_stack.pop()
print("Popped: {}".format(popped))
print("New top: {}".format(my_stack.peek()))

popped = my_stack.pop()
print("Popped: {}".format(popped))
print("New top: {}".format(my_stack.peek()))

popped = my_stack.pop()
print("Popped: {}".format(popped))
print("New top: {}".format(my_stack.peek()))

my_stack.print_list()