def lengthOfLIS(nums):
        #TC O(N^2) SC O(N)
        n = len(nums)
        dp = [1] * n
        if not nums: return 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))