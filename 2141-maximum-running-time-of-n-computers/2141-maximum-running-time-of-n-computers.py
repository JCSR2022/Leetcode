class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        #binary search aproach 

        l, r, ans=min(batteries), sum(batteries)//n, 0
        while l<=r:

            mid=(l+r)>>1
            reserve=0
            for x in batteries: 
                reserve+=min(x, mid)
            
            #print((l,mid,r),reserve,mid*n,ans )
            if reserve>=mid*n:
                ans=mid
                l=mid+1
            else:
                r=mid-1
                
        #print((l,mid,r),reserve,mid*n,ans )    
        return ans

#----------------------------------------------------------------
        #brute force aproach:
        # make heap and pop n reduce by 1 all ,repeat until 0//

        # heap = []
        # for bat in batteries:
        #     heapq.heappush(heap,-bat) 
        # #print(heap)
        # count = 0
        # while True:
        #     bat_to_use = []
        #     for _ in range(n):
        #         curr_bat = heapq.heappop(heap)
        #         if curr_bat == 0:
        #             return count
        #         bat_to_use.append(curr_bat+1)
        #     #print(bat_to_use)
        #     for bat in bat_to_use:
        #         heapq.heappush(heap,bat)
        #     #print(heap)
        #     count +=1

#Time Limit Exceeded 
#----------------------------------------------------------------------       





#----------------------------------------------------
        #sum all batteries and // by n??
        #return sum(batteries)//n
#do not work

