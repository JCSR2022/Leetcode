class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        #Orgniza balls so the distance between them is max , return min dist posible//
        
        position.sort()
        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        ans = 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.canWePlace(position, mid, m):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans
    
    def canWePlace(self, arr, dist, balls):
        countBalls = 1
        lastPlaced = arr[0]
        for i in range(1, len(arr)):
            if arr[i] - lastPlaced >= dist:
                countBalls += 1
                lastPlaced = arr[i]
            if countBalls >= balls:
                return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
# have no brain now      
#         # first option : fid max of psoitions, return maxP//m ??      
#         max_p = max(position)
#         min_p = min(position)
        
#         ans =  (max_p-min_p)%(m)
#         print(max_p-min_p,m-1,ans)
#         if  ans == 0:
#             ans = (max_p-min_p)//(m-1)

#         return ans


        

