def findMin(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        # min_value = float('inf')
        # for num in nums:
        #     min_value = min(min_value, num)
        # return min_value
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while left <= right:
            mid = left + right // 2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid -1

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))