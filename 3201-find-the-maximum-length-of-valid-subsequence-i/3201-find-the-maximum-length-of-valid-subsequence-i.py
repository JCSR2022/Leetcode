class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        #brute force 2**n
        #una mierda!!!!jajajaja

        # N = len(nums)
        # posibles = set()
        # for n in range(2**N):
        #     sub = [ v  for v,d in zip(nums,bin(n)[2:].zfill(N)) if d =='1']
        #     if len(sub)>=2:
        #         posibles.add(tuple(sub))
        
        # ans = 0
        # for sub in sorted(list(posibles)):
        #     is_valid = True
        #     sub_odd = (sub[0]+sub[1])%2
        #     for i in range(1,len(sub)-1):
        #         if (sub[i]+sub[i+1])%2 != sub_odd:
        #             is_valid = False
        #     if is_valid:
        #         ans = max(ans,len(sub))
        #     print(sub, ans)
        # return ans

# Time Limit Exceeded , what a surprise jajajaj
#---------------------------------------------------

        #This about odd and even sum, sum(evens) =even, and same to odd
        # chage to 1,0 arr, even odd, 
        #find max seq 1,0 or 0,1, or 0,0 or 1,1

        odd_num = [ n%2 for n in nums]
        ans = max(odd_num.count(0),odd_num.count(1))

        prev = odd_num[0]
        count = 1
        for i in range(1,len(odd_num)):
            if odd_num[i] != prev:
                count += 1    
                prev = odd_num[i] 

        ans = max(ans,count)

        return ans 
        