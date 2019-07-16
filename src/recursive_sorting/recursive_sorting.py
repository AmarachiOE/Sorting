# TO-DO: complete the helper function below to merge 2 sorted arrays into a new completely sorted array
def merge( arrA, arrB ):
    # setting the total expected # of elements there will be
    elements = len( arrA ) + len( arrB ) 

    # setting a new empty array with length to fit the expected number of elements (placeholder 0)
    merged_arr = [0] * elements 

    # TO-DO

    # initialize values at index 0
    i, j , k = 0, 0, 0
    
    # looping through the elements in array A and array B (left and right sublists of original array)
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]: # if the ith elem is less than or equal to the jth elem, add i to first position in merged array merged_arr[k] = merged_arr[0]
            merged_arr[k] = arrA[i]
            i += 1 # move to next ith elem
        else: # if j is less than i, add j instead
            merged_arr[k] = arrB[j]
            j += 1 # move to next jth elem
        k += 1 # move to next kth elem

    while i < len(arrA): # while i is within range of arrA
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB): # while j is within range of arrB
        merged_arr[k] = arrB[j]
        j += 1
        k += 1


    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        
        mid = len(arr) // 2 # find mid point of array
        left = arr[:mid] # set left half
        right = arr[mid:] # set right half

        left_sorted = merge_sort(left) # recursion - left array is sorted now       
        right_sorted = merge_sort(right) # recursion - right array is sorted now

        # reset the passed in array as the now sorted array
        arr = merge(left_sorted, right_sorted) 

        # print("Sorted Left: ", left_sorted)
        # print("Sorted Right: ", right_sorted)
        # print("Final Array: ", arr)

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
merge_sort(arr1)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


"""
or combine setting left + right with recursive  steps like:

left = merge_sort(arr[:mid]) # Recursion: set left half and sort it

right = merge_sort(arr[mid:]) # Recursion: set right half and sort it

then arr = merge(left, right)
"""