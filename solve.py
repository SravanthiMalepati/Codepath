# def solve(nums, target):
#     i, j = 0, len(nums) - 1
#     output = [target] * len(nums)
#     for k in range(len(nums)):
#         if nums[k] < target:
#             output[i] = nums[k]
#             i += 1
#         elif nums[k] > target:
#             output[j] = nums[k]
#             j -= 1
#     return output

#time & space is O(n)
def solve(nums, target):
    i, j = 0, 1
    while j < len(nums):
        if nums[i] < target:
            i += 1
        elif nums[j] < target:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    j -= 1
    while i < j:
        if nums[j] > target:
            j -= 1
        elif nums[i] > target:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i += 1
    return nums
#time is o(n), space is O(1)
nums = [9,12,5,10,14,3,10]
target = 10
print(solve(nums,target))