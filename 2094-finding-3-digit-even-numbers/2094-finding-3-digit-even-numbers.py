class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        #aproach n**3

        # N = len(digits)

        # ans = []
        # for i in range(N):
        #     for j in range(i+1,N):
        #         for k in range(j+1,N):
        #             if digits[i] != 0 and digits[k]%2 == 0:
        #                 ans.append( digits[i]*100+digits[j]*10+digits[k])
        
        # return ans
        
        #nooooooooooooooooooooooooo
#--------------------------------------------------------------------


        # ans = []
        # for num in set(itertools.permutations(digits, 3)):
        #     if num[0] !=0  and num[2]%2 == 0:
        #         ans.append(num[0]*100+num[1]*10+num[0]  )
        # ans.sort()
        # return ans

        #noooooooooooooooooooooooooooooooooooooo
#-----------------------------------------------------------

        #aproach n**3

        # N = len(digits)

        # ans = set()
        # for i in range(N):
        #     for j in range(i+1,N):
        #         for k in range(j+1,N):
        #             if digits[i] != 0: 
        #                 if digits[j]%2 == 0:
        #                     ans.add( digits[i]*100+digits[k]*10+digits[j])
        #                 if digits[k]%2 == 0:
        #                     ans.add(digits[i]*100+digits[j]*10+digits[k])
        #             if digits[j] != 0:
        #                 if digits[k]%2 == 0:
        #                     ans.add(digits[j]*100+digits[i]*10+digits[k])
        #                 if digits[i]%2 == 0:
        #                     ans.add(digits[j]*100+digits[k]*10+digits[i])
        #             if digits[k] != 0:
        #                 if digits[i]%2 == 0:
        #                     ans.add(digits[k]*100+digits[j]*10+digits[i])
        #                 if digits[j]%2 == 0:
        #                     ans.add(digits[k]*100+digits[i]*10+digits[j])
        # ans =list(ans)
        # ans.sort()
                
        # return ans
# 1763 ms,  Beats 41.62%
#-------------------------------------------------------

        N = len(digits)
        ans = set()
        for i in range(N):
            if digits[i] != 0:
                for j in range(N):
                    if j != i:
                        for k in range(N):
                            if k != i and k != j and digits[k]%2 == 0:
                                ans.add( digits[i]*100+digits[j]*10+digits[k] )
        return sorted(list(ans))