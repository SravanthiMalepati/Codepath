def sortnumber(nums):
 
    for i in range(len(nums)):
        for j in range(0,len(nums)-1):
            if nums[j] < nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp 
            else:
                continue
    return nums

    
print(sortnumber([10,5,20,15]))