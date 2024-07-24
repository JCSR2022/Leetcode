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
            map_num = [ mapping[int(n)]*(10**i) for i,n in enumerate(str(num)[::-1]) ]
            return  sum(map_num)
        
        return sorted(nums,key = lambda x: mapingFunc(x,mapping))

    
            
            
        