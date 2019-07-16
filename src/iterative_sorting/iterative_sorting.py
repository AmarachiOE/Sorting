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
print("Bubble Sort: ", result)


# STRETCH: implement the Count Sort function below
# Example from w3schools
# Check out: https://visualgo.net/en/sorting

def count_sort( arr, maximum=1):
    #maximum = max(arr)
    m = maximum + 1
    count = [0] * m # creating empty array to keep count of freq

    for i in arr:
        # count number of occurences of each elem in arr
        count[i] += 1

    val = 0

    for i in range(m):
        for j in range(count[i]):
            arr[val] = i
            val += 1

    return arr

array1 = [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1]
print("Original Array: ", array1)
print("Count Sort: ", count_sort(array1, 7 ))


def count_sort2( arr, maximum=-1 ):
    output = [0 for i in range(256)] # will have sorted arr
    count = [0 for i in range(256)] # stores indiv counts of each charac in arr
    ans = ["" for _ in arr] # stores resulting answer 

    # store count of each character
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual 
    # position of this character in output array 
    for i in range(256): 
        count[i] += count[i-1]

    # Build the output character array 
    for i in range(len(arr)): 
        output[count[arr[i]]-1] = arr[i] 
        count[arr[i]] -= 1

    # Copy the output array to arr, so that arr now 
    # contains sorted characters 
    for i in range(len(arr)): 
        arr[i] = output[i]

    return arr

"""
example:
arr = "geeksforgeeks"
result = count_sort2(arr)
print("Count Sort: ", result) # Count Sort: eeeefggkkorss
"""