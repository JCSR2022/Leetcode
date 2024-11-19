class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        # #brute force:Time Limit Exceeded
        # max_sum = 0
        # for i in range(0,len(nums)-k+1):
        #     arr = nums[i:i+k] 
        #     if  len(set(arr)) == k:
        #         max_sum = max(max_sum,sum(arr))
        # return max_sum
    
#----------------------------------------------------------

        #sliding window//hashMap: Time Limit Exceeded
    
       
        
#         hashMap = Counter(nums[0:k])
      
#         if len(nums) == k:
#             if len(hashMap.keys()) == k:
#                 return sum(nums)
#             else:
#                 return 0
            
#         ans = 0
#         if len(hashMap) == k:
#             ans = max(ans,sum(hashMap.keys()))
        
#         for i in range(1,len(nums)-k+1):
#             hashMap[nums[i-1]] -=1
#             hashMap[nums[i+k-1]] +=1
#             if hashMap[nums[i-1]] == 0: hashMap.pop(nums[i-1], None)
#             #print(nums[i:i+k],hashMap)
#             if len(hashMap) == k:
#                 ans = max(ans,sum(hashMap.keys()))
        
#         return ans
            

#---------------------------------------------------
# https://www.youtube.com/watch?v=pT-lOE1on3M

        res = 0
        count = defaultdict(int)
        cur_sum = 0

        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            count[nums[r]] +=1

            if r - l + 1 > k:
                count[nums[l]] -=1
                if count[nums[l]] == 0: count.pop(nums[l], None)
                cur_sum -= nums[l]
                l += 1

            if len(count) == r - l + 1 == k:
                res = max(res,cur_sum)


        return res
    
    
    
    
    


    
    
    
    