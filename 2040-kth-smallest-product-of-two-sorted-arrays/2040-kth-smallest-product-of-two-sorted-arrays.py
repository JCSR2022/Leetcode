class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        #Brute force O(n**2)+ n**2log(n)
        #will not work do time
        ans = []
        for n1 in  nums1:
            for n2 in nums2:
                ans.append(n1*n2)
        ans.sort()
        return ans[k-1]