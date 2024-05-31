class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
#         #brute force  Time O(n)  space O(n)
#         hashMap = defaultdict(int)
#         for n in nums:
#             hashMap[n] += 1
        
#         ans = []
#         for key,val in hashMap.items():
#             if val == 1:
#                 ans.append(key)
#         return ans

        #xor solution time O(n) sapace O(1) ??
     
        # XOR of list while return xor of only diff nums
        xor =  0
        for n in nums:
            xor ^= n 
        
        
        # Finding bits that differ
        diff_bit = 1 
        while not (xor & diff_bit):
            diff_bit = diff_bit << 1
            
        a,b = 0,0
        
        for n in nums:
            if diff_bit & n:
                a = a ^ n
            else:
                b = b ^ n
                
        return [a,b]
                
            
            
            
            
            
        