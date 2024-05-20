class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # brute fore sorting: O(n) = nlog(n)
        nums.sort()
        return nums[-k]
        
        
        
        