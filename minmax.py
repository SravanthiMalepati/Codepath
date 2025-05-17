# Given an array of size N. The task is to find the maximum 
# and the minimum element of the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1 Maximum element is: 9


# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3 Maximum element is: 35

def minmax(arr):
    n = len(arr)
    min_value = arr[0]
    max_value = arr[0]
    for i in range(1,n):
        min_value = min(min_value,arr[i])
        max_value = max(max_value,arr[i])
    return min_value,max_value

print(minmax([3, 5, 4, 1, 9]))
print(minmax([22, 14, 8, 17, 35, 3]))