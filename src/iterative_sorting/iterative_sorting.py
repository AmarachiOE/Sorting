# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    
    # loop through n-1 elements
    for i in range(0, len(arr) - 1): 
        smallest_index = i

        
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc - lines of code) 
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                smallest_index = j
                 
                # TO-DO: swap
                arr[smallest_index], arr[i] = arr[i], arr[smallest_index]


    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print("Original Array: ", arr1)
result = selection_sort(arr1)
print("Selection Sort: ", result)



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)

    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr)):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j] # simple swap

    return arr

arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print("Original Array: ", arr2)
result = bubble_sort(arr1)
print("Selection Sort: ", result)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr