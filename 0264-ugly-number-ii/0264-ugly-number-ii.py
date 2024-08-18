import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
#         #using minheap and add all num that can be created untill reach n
#         ans = [1]
#         nums = [2,3,5]
#         heapq.heapify(nums)
        
#         while len(ans) < n: 
#             #print("nums:",nums)
#             x = heapq.heappop(nums)
#             ans.append(x)
#             for i in [2,3,5]:
#                 if i*x not in nums:
#                     heapq.heappush(nums,i*x)

#         return ans[-1]


        #improve: Time nLog(n)
    
#         nums = [1]
#         visit = set()
        
#         for i in range(n):
#             x = heapq.heappop(nums)
            
#             for i in [2,3,5]:
#                 if x*i not in visit:
#                     visit.add(x*i)
#                     heapq.heappush(nums, x*i)
            
#         return x  
            
            
        #three pointers O(n):
        
        nums = [1]
        
        i2,i3,i5 =0,0,0
        
        for i in range(1,n):
            next_num = min(nums[i2]*2 ,nums[i3]*3 ,nums[i5]*5 )
            nums.append(next_num)
            
            if next_num == nums[i2] * 2:
                i2 += 1
            if next_num == nums[i3] * 3:
                i3 += 1    
            if next_num == nums[i5] * 5:
                i5 += 1
        

        return nums[-1]
        
        
            
            
            
            
            
            
            
            
            
            
            
            
    

        
        
        