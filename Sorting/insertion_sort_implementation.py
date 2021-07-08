def insertion_sort(numbers:list):
    for i in range(len(numbers)):
        if numbers[i] <= numbers[0]:
            # numbers.append(numbers[i])
            numbers.insert(0, numbers.pop(i))
        else:
            for j in range(1, i):
                if numbers[j-1] <= numbers[i] <= numbers[j]:
                    numbers.insert(j, numbers.pop(i))

    return numbers

unsorted_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# unsorted_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# unsorted_numbers = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0]
# unsorted_numbers = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]
# unsorted_numbers = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

sorted_numbers = insertion_sort(unsorted_numbers)
print("Final output: ")
print(sorted_numbers)