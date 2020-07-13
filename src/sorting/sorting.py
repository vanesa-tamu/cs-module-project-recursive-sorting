# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here

    # copy all elements of arrA and to merged_arr
    # merged_arr = arrA[:]
    # print(f'merged_arr now: {merged_arr}')

    # Traverse arrB and arrA simultaneously, one by one
    # copy smaller element to next position in arr3[]
    # and move ahead in arr3[] and the array whose element is picked.
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:  # arrB[j] < arrA[i]
            merged_arr[k] = arrB[j]
            j += 1
        # increment K
        k += 1

    # if there are any remaining elements in both arrays:
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


arr_a = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr_b = [0, 1, 2, 3, 4, 5]
print(merge(arr_a, arr_b))  # [0, 1, 1, 2, 3, 4, 5, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO: implement the Merge Sort function below recursively
# Base Case: Array is sorted


def merge_sort(arr):
    print(f'Array at first: {arr}')
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # sort left and right values
        l = merge_sort(left) if len(left) > 1 else left
        r = merge_sort(right) if len(right) > 1 else right
    # merge the sorted left and right sides of arr
    else:
        return arr

    return merge(l, r)


arr_c = [1, 0, 0, 0]
# print(merge_sort(arr_c))
print(merge_sort(arr_a))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here

