def longestConsecutiveSubsequence(arr):
    # res = 1
    # curr = 1
    # arr.sort()
    # if len(arr) == 0: return 0
    # for i in range(1,len(arr)):
    #     if arr[i] == arr[i-1]:
    #         continue
    #     elif arr[i] == arr[i-1] +1:
    #         curr += 1
    #     else:
    #         curr = 1
    #     res = max(res,curr)
    # return res
    
    array = set(arr)
    # print(array)
    res = 0
    for val in arr:
        if val in array and (val-1) not in array:
            curr = val
            cnt = 0
            while curr in array:
                array.remove(curr)
                cnt += 1
                curr += 1
            res = max(res,cnt)
    return res

print(longestConsecutiveSubsequence([1,9,3,10,4,20,2])) #4
print(longestConsecutiveSubsequence([36, 41, 56, 35, 44, 33, 34, 43, 92, 32, 42])) #5
print(longestConsecutiveSubsequence([2])) #1
print(longestConsecutiveSubsequence([])) #0
print(longestConsecutiveSubsequence([3, 9, 50, 2, 8, 4, 1])) #4
print(longestConsecutiveSubsequence([1, 5, 29, 4, 3, 2, 1])) #5