class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        
        new_arr = []
        for num in arr:
            if num not in new_arr:
                new_arr.append(num)
        arr = new_arr
        #brute force n**2
        n = len(arr)
        ans = set()
        for i in range(n):
            currBitOr = arr[i]
            for j in range(i,n):
                currBitOr |= arr[j]
                ans.add(currBitOr)
        return len(ans)         

#Time Limit Exceeded
#--------------------------------------------------------
     #make bit_mask and update if any bit of new n not in bitmask +1










# ------------------------------------------------        
   

