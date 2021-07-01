# Write two functions that finds the factorial of any number.
# One should use recursion, the other should just use a for loop.


def find_factorial_recursive(input_val):
    if input_val == 1 or input_val == 0:
        return 1  # Base case
    else:
        return input_val * find_factorial_recursive(input_val-1)  # recursive case


def find_factorial_iterative(input_val):
    answer = 1
    while input_val > 1:
        answer *= input_val
        input_val -= 1
    return answer


input_val = 7
print(find_factorial_recursive(input_val))
print(find_factorial_iterative(input_val))