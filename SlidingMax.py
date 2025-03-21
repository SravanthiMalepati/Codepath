from collections import deque
def maxSlidingWindow( nums, k):
        
        n = len(nums)

        res = []
        
        if not nums and k == 0:
            return res
        dq = deque()

        l, r = 0,0
        while r < n:
            while dq and nums[r] >= nums[dq[-1]]:
                dq.pop()
            dq.append(r)
            if dq[0] < l:
                dq.popleft()
            if r+1 >= k:
                res.append(nums[dq[0]])
                l += 1
            r += 1
        return res 
        # for i in range(n):
        #     if dq and dq[0] < i - k + 1:
        #         dq.popleft()
        #     while dq and nums[dq[-1]] < nums[i]:
        #         dq.pop()
        #     dq.append(i)
        #     if i >= k - 1:
        #         res.append(nums[dq[0]]) 
        # return res

        # for i in range(n-k+1):
        #     res.append(max(nums[i:i+k]))
        # return res
        

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))