unsorted_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# unsorted_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# unsorted_numbers = [8, 9, 7, 6, 5, 4, 3, 2, 1, 0]
# unsorted_numbers = [0, 1, 2, 3, 4, 9, 8, 7, 6, 5]
# unsorted_numbers = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]


def bubble_sort(numbers:list):
    has_list_updated = True
    step_counter = 0

    while has_list_updated:
        has_list_updated = False

        for i in range(len(numbers)-1):
            if numbers[i+1] < numbers[i]:
                temp = numbers[i+1]
                numbers[i + 1] = numbers[i]
                numbers[i] = temp
                has_list_updated = True
            step_counter += 1

        print(numbers)
    print("Stepped {} times".format(step_counter))
    return numbers


sorted_numbers = bubble_sort(unsorted_numbers)
print("Final output: ")
print(sorted_numbers)