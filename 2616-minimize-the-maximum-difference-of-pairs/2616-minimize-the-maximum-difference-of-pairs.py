class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        #firs sort, then make min_heap with pairs  (i,j) if use disreagd
        #nlog(n)

        if p == 0:
            return 0

        
        nums.sort()
        count = 0
        ans = float("-inf")
        while  count < p:
            N = len(nums)
            heap = []
            for i in range(N-1):
                heapq.heappush(heap,( abs(nums[i]-nums[i+1]) ,i,i+1))

            # print(nums)
            # print(heap)
            used = set()
            
            while heap:
                cur_diff,i,j = heapq.heappop(heap)
                #print(count,cur_diff,i,j,used,heap,ans)

                if i in used or j in used:
                    continue
                used.add(i)
                used.add(j)

                ans = max(ans,cur_diff)
                count += 1
                if count == p:
                    return ans

            nums = [nums[i] for i in range(N) if i not in used]
            #print(nums)

        


#----------------------------------








        