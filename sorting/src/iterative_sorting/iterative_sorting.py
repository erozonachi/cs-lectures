# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        smallest_element = arr[smallest_index]
        for j in range(i+1, len(arr)):
            if arr[j] < smallest_element:
                smallest_element = arr[j]
                smallest_index = j

        # TO-DO: swap
        if i != smallest_index:
            arr[smallest_index] = arr[i]
            arr[i] = smallest_element

    return arr


print(selection_sort([5, 8, 2, 6, 9, 4, 3, 7, 1]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
