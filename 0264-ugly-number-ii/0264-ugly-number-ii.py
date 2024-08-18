import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        #using minheap and add all num that can be created untill reach n
        

        ans = [1]
        nums = [2,3,5]
        heapq.heapify(nums)
        
        while len(ans) < n: 
            #print("nums:",nums)
            x = heapq.heappop(nums)
            ans.append(x)
            for i in [2,3,5]:
                if i*x not in nums:
                    heapq.heappush(nums,i*x)

        return ans[-1]

        
        
        