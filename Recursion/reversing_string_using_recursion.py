
def reverse_str(in_str):
    if len(in_str) == 0:
        return in_str

    if len(in_str) == 1:  # in C/C++ would have looked for null termination instead
        return in_str
    else:
        return reverse_str(in_str[1:]) + in_str[0]


print(reverse_str(" 123 456 "))
