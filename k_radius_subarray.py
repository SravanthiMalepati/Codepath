def getAverages(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0: return nums
        n = len(nums)
        result = [-1] * n
        window = 2*k + 1
        if window > n: return result
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range(k,n-k):
            l,r = i -k, i + k
            sum1 = prefix[r+1]-prefix[l]
            res = (sum1 // window)
            result[i] = res
        return result


print(getAverages([7,4,3,9,1,8,5,2,6],3))
print(getAverages([100000],0))
print(getAverages([8],10000))