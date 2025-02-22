def majorityElements(nums):
    d = { }
    for i in nums:
        if i in d.keys():
            counter = d[i] + 1
            d[i] = counter
        else:
            counter = 1
            d[i] = counter
    for key,values in d.items():
        if values > len(nums) /2:
            return key
        return -1
    
print(majorityElements([3,2,3])) #3
print(majorityElements([2,2,1,1,1,2,2])) #2