class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # #first will find k, rotation
        # #2do do binary search?

        # def findRotationK():
        #     l = 0
        #     r = len(nums)-1

        #     if nums[r]>nums[l]:
        #         return 0

        #     while r>l:
        #         m = (r+l)//2

        #         if nums[m] < nums[l]:
        #             r = m - 1
        #         else:
        #             l = m + 1

        #     return m
                    

        # #eres un maldito imbecil que no sirve apra nada, deberias suicidarte para acabar con tu miserable vida!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111




        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
        