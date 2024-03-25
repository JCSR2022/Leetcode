class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # aproach hashTable
        
        c = Counter(nums)
        
        return [ key for key,value in c.items() if value >1 ] 
     