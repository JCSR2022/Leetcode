# class Solution:
#     def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        #brute force, somthing like booble sort?

        # change = True
        # while change:
        #     change = False
        #     for i in range(len(nums)):
        #         for j in range(i,len(nums)):
        #             if ((nums[j] < nums[i]) and  (nums[i]-nums[j] <= limit)) :    
        #                 nums[j],nums[i] = nums[i],nums[j]
        #                 change = True

        # return nums

#Time Limit Exceeded, of course!!!! Imbecil, y no tienes tiempo para pensarlo, idiota!!!
#----------------------------------------------------------------------


#eunice
class Solution:
    def lexicographicallySmallestArray(self, A: list[int], limit: int) -> list[int]:
        
        groups = []
        gmap = {}

        for val in sorted(A):
            if not groups or val - groups[-1][-1] > limit:
                groups.append([])
            groups[-1].append(val)
            gmap[val] = len(groups) - 1

        itr = [iter(g) for g in groups]

        for i in range(len(A)):
            A[i] = next(itr[gmap[A[i]]])

        return A
