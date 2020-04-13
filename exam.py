name = str(input("What is your name: "))  # Ask the name of the user
count = int(input("How many integers do you want in the list: "))  # To ask how many integers in the list user wants
array = []  # list to save the integers
while True:  # Keep asking to fill the integers in the list
    ask = str(input(f'What is your integer {count} integer: '))  # Input of the user for the integers
    count -= 1   # count -1 in order to stop the loop
    array.append(ask)  # appending my integers to the list
    if count == 0:  # statement if the count is 0 when should stop WHILE loop
        print(array)  # printing the array
        array = [int(i) for i in array]  # Converting str to int
        print(array)  # printing the integer list!
        break  # Break statement to finish the process

option = int(input("what type of sort do u wanna use? 1.Bubble: "
                   "2.Selection 3.Insertion 4.Merge 5.Quick "))  # Asking the user of option to sort the list
if option == 1: # if user will check 1
    def bubble_sort(array):  # Bubble sorting function
        def swap(i, j):  # divides by i and j in order to replace the places
            array[i], array[j] = array[j], array[i]  # arr i can be arr j and arr j can be arr i

        n = len(array)  # N length of the array
        swapped = True  # Condition is True

        x = -1  # -1 to have sequence to compare
        while swapped:  # the process of swiping
            swapped = False  # swapped is false
            x = x + 1  # sequence
            for i in range(1, n - x):  # looping through 1 to till the condition is True
                if array[i - 1] > array[i]:  # Condition when i -1 is bigger than just i
                    swap(i - 1, i)  # swapping and the function works again
                    swapped = True  # then it becomes True
        return array  # returning array
    print("Bubble sorting...")  # To print bubble sorting
    print(bubble_sort(array))  # calling the function
elif option == 2:  # if user will check 2
    def selection_sort(array):  # selection sort function
        for i in range(len(array)):  # Looping through len of this array
            minimum = i  # Minimum becomes i, we need minimum to compare with other numbers

            for j in range(i + 1, len(array)):  # looping through sequence +1 to ech index
                # Select the smallest value
                if array[j] < array[minimum]:  # condition if j is bigger than minimum, we will have new minimum J
                    minimum = j  # Now, J becomes new minimum

            # Place it at the front of the sorted end of the array
            array[minimum], array[i] = array[i], array[minimum]
        return array  # returning the array

    print("Selection sorting...")  # printing selection sorting
    print(selection_sort(array))  # calling the function
elif option == 3:  # if the user will check 3
    def insertion_sort(array):  # insertion function

        for i in range(len(array)):  # loop through length of array
            cursor = array[i]  # cursor becomes the looping numbers in the index
            pos = i  # pos is become i

            while pos > 0 and array[pos - 1] > cursor:  # while loop through if pos is bigger and array with -1 index bigger than cursor(curso is the nmbers in the loop)
                # Swap the number down the list
                array[pos] = array[pos - 1]
                pos = pos - 1

            array[pos] = cursor

        return array  # returning array

    print("Insertion sorting...")  # printing insertion array
    print(insertion_sort(array))  # calling the insertion function
elif option == 4:  # if the user will check 4
    def merge_sort(array):  # Merge sorting function
        # The last array split
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        # Perform merge_sort recursively on both halves
        left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

        # Merge each side together
        return merge(left, right, array.copy())


    def merge(left, right, merged):  # merged function

        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):

            # Sort each one and place into the result
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor + right_cursor] = left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1

        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]

        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]

        return merged

    print("Merge sorting...")  # printing merge sorting
    print(merge_sort(array))   # calling the merge function
elif option == 5:  # if the user will check 5
    def partition(array, begin, end):
        pivot_idx = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx


    def quick_sort_recursion(array, begin, end):
        if begin >= end:
            return
        pivot_idx = partition(array, begin, end)
        quick_sort_recursion(array, begin, pivot_idx - 1)
        quick_sort_recursion(array, pivot_idx + 1, end)
        return array


    def quick_sort(array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        return quick_sort_recursion(array, begin, end)

    print("Quick sorting...")  # printing the quick sort
    print(quick_sort(array))   # printing the result of sorted list


def thank_you(name):  # thank you function
    print(f"Thank you {name} for testing my project.")  # printing thank you with name input


thank_you(name)  # calling thank you function

















