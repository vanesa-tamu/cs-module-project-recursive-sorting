# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    if arrA[0] > arrB[0]:
        merged_arr.append(arrB)
        merged_arr.append(arrA)
    else:
        merged_arr.append(arrA)
        merged_arr.append(arrB)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:  # base case
        return arr
    else:
        # find the middle:
        middle_i = (len(arr) // 2) - 1
        # divide in half:
        left_a = arr[:middle_i]
        right_a = arr[:middle_i]
        # merge_sort on the 2 new arrays:
        left_merge = merge_sort(left_a) if len(left_a) > 1 else left_a
        right_merge = merge_sort(right_a) if len(right_a) > 1 else right_a
    # once base case is hit, will start to merge arrays
    return merge(left_a, right_a)

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

