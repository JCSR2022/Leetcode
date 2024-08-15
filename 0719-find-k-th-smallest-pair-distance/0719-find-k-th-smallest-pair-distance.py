class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        #aproach , brute force
        #len(nums)
        # ans =[]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         print(i,j,[nums[i],nums[j]],abs(nums[i]-nums[j]))
        #         ans.append(abs(nums[i]-nums[j]))            
        # ans.sort()
        # return ans[k-1]
        
        #l8q4 , binary search aproach 
        #https://www.youtube.com/watch?v=BZpF_o60STI
        def cnt_pair(d):
            cnt = 0
            for i in range(n-1):
                cnt += bisect.bisect(nums, nums[i] + d)
            return cnt

        n = len(nums)
        p = k + n * (n-1) // 2
        nums.sort()
        a, b = 0, nums[-1] - nums[0]
        while a <= b:
            d = (a+b) // 2
            cnt = cnt_pair(d)
            if p <= cnt:
                b = d - 1
            else:
                a = d + 1
        return a