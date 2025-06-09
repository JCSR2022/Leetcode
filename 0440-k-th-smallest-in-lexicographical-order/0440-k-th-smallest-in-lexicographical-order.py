class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        #build lexigrapical until k, O(n) Time problem n = 10**9

        # p = 0
        # def recurrency(num):
        #     nonlocal p
        #     #print(p,num)
        #     if p == k-1:
        #         return num

        #     for i in [0,1,2,3,4,5,6,7,8,9]:
        #         new_num = num*10+i 
        #         if new_num <= n:
        #             p += 1
        #             ans = recurrency(new_num)
        #             if ans:
        #                 return ans

        #     if num < 9 :
        #         p += 1
        #         return recurrency(num+1)

        # return recurrency(1)

#Time Limit Exceeded 
#-------------------------------------------------------------
        #https://www.youtube.com/watch?v=wRubz1zhVqk

        cur  = 1
        i = 1

        def count(cur):
            res = 0
            nei = cur + 1
            while cur <= n:
                res += min(nei,n+1) - cur
                cur *= 10
                nei *= 10
            return res

        while i < k:                
            steps = count(cur)
            if i + steps <=k:
                cur = cur + 1
                i += steps
            else:
                cur *= 10
                i += 1

        return cur
            



        