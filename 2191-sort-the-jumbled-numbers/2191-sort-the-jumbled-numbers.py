class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        
#         def mapingFunc(num,mapping):
#             num = list(str(num))
#             ans = [ str(mapping[int(n)]) for n in num ]
#             return int("".join(ans))

        # def mapingFunc(num,mapping):
        #     ans = [ str(mapping[int(n)]) for n in str(num) ]
        #     return int("".join(ans))
        
        def mapingFunc(num,mapping):
            map_num = [ mapping[int(n)] for n in str(num) ]
            ans = 0
            for i,n in enumerate(map_num[::-1]):
                ans += (10**i)*n
            return  ans
        
        return sorted(nums,key = lambda x: mapingFunc(x,mapping))

    
            
            
        