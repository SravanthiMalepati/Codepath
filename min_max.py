#Finding maximum number out of minimum from buckets 
# of k size from an unsorted array.
def min_max(arr,k):
    n = len(arr)
    max_value = 0
    sub_arr = []
    for i in range(0,n-2):
        sub_arr.append(arr[i:i+k])
    print(sub_arr)
    # return max(min_value)
    

print(min_max([1,3,4,6,2,9,8],2))
print(min_max([1,3,4,6,2,9,8],3))