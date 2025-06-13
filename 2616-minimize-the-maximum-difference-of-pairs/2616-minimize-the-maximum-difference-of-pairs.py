class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        if p == 0:
            return 0

        def isValid(threshold):
            i,cnt = 0,0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= threshold:
                    cnt += 1
                    i   += 2
                else:
                    i += 1
                if cnt == p:
                    return True
            return False

        nums.sort()
        l,r = 0, max(nums)
        ans = max(nums)

        while l <= r:
            m = l +(r-l)//2
            if isValid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans
#-----------------------------------------------------------
        #sort and use binary search

        # N = len(nums)
        # nums.sort()

        # def is_max(n):
        #     count = 0
        #     i = 0
        #     while i <= N-1:
        #         if abs(nums[i]-nums[i+1]) <= n:
        #             count +=1
        #             i +=2
        #         else:
        #             i += 1
            

        # r = 0


#---------------------------------------------------------
        #firs sort, then make min_heap with pairs  (i,j) if use disreagd
        #nlog(n)

        # if p == 0:
        #     return 0

        
        # nums.sort()
        # count = 0
        # ans = float("-inf")
        # while  count < p:
        #     N = len(nums)
        #     heap = []
        #     for i in range(N-1):
        #         heapq.heappush(heap,( abs(nums[i]-nums[i+1]) ,i,i+1))

        #     # print(nums)
        #     # print(heap)
        #     used = set()
            
        #     while heap:
        #         cur_diff,i,j = heapq.heappop(heap)
        #         #print(count,cur_diff,i,j,used,heap,ans)

        #         if i in used or j in used:
        #             continue
        #         used.add(i)
        #         used.add(j)

        #         ans = max(ans,cur_diff)
        #         count += 1
        #         if count == p:
        #             return ans

        #     nums = [nums[i] for i in range(N) if i not in used]
        #     #print(nums)

        

#no funciona imbecil!!!
#----------------------------------








        