# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fibonacci_iterative(idx):
    last = 1
    second_last = 0

    if idx < 2:
        return idx

    for i in range(2, idx+1):
        n = last + second_last
        second_last = last
        last = n
    return n


def fibonacci_recursive(idx):
    if idx < 2:
        return idx
    else:
        return fibonacci_recursive(idx-1) + fibonacci_recursive(idx-2)


index = 5
print(fibonacci_iterative(index))
print(fibonacci_recursive(index))