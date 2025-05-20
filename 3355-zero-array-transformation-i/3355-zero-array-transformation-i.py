class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # N = len(nums)
        # reduct = [0]*N

        # for li, ri in queries:
        #     for i in range(li, ri+1):
        #         reduct[i] += 1

        # for i in range(N):
        #     if nums[i]-reduct[i] > 0:
        #         return False
        # return True     
      
#Time Limit Exceeded
#--------------------------------------------

        N = len(nums)
        reduct = [0]*(N+1)

        for li, ri in queries:
            reduct[li]   +=1
            reduct[ri+1] -=1

        count = 0
        for i in range(N):
            count += reduct[i]
            if nums[i]-count > 0:
                return False

        return True  














#---------------------------------

        # N = len(nums)
        # f = [0]*(N+1)

        # for s,e in queries:
        #     f[s] += 1
        #     f[e+1] -=1
        # print(f)
        # for i in range(1,N+1):
        #     f[i] += f[i-1]
        # print(f)
        # for i in range(N):
        #     if nums[i] > f[i]:
        #         return False
        # return True 