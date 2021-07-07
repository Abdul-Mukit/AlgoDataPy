def selectionSort(numbers:list):

    for i in range(len(numbers)):
        cur_min_idx = i
        cur_min = numbers[i]

        for j in range(i, len(numbers)):
            if numbers[j] < cur_min:
                cur_min = numbers[j]
                cur_min_idx = j
                print("cur min " + str(cur_min))

        numbers[cur_min_idx] = numbers[i]
        numbers[i] = cur_min
        print(numbers)
    return numbers

# unsorted_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# unsorted_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# unsorted_numbers = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0]
# unsorted_numbers = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]
unsorted_numbers = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

sorted_numbers = selectionSort(unsorted_numbers)
print("Final output: ")
print(sorted_numbers)

