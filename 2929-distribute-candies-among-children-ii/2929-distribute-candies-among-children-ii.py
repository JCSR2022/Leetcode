class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        childs = 3

        if n > limit*childs:
            return 0 

        #brute force, stupid way: n**3

        # count = 0 
        # ans = []
        # for i in range(limit+1):
        #     for j in range(limit+1):
        #         for k in range(limit+1):
        #             if sum((i,j,k)) == n:
        #                 ans.append((i,j,k))
        #                 count +=1 
        # print(ans)
        # return count

#--------------------------------------------

        #brute force, lees stupid : n**2

        # count = 0 
        # ans = []
        # for i in range(limit+1):
        #     for j in range(limit+1):
        #         k = n-i-j
        #         if k >= 0 and k <= limit :
        #             ans.append((i,j,k))
        #             count +=1 
        # print(ans)
        # return count
#-------------------------------------------------------------
        total = 0
        for c in range(min(n+1,limit+1)):
            i = n-c
            if i >= 0 and i<= limit*2:
                total += min(i,limit*2-i)+1

        return total 

