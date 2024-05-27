class Solution:
    def specialArray(self, nums: List[int]) -> int:
        #maldita sea brute force
        
        for i in range(len(nums)+1):
            cont = 0
            for n in nums:
                if n >= i: cont +=1
            #print(i,cont)
            if i == cont:
                return i
        
        return -1
        