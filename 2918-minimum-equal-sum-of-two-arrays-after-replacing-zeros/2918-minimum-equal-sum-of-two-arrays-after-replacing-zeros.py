class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        

        #aproach , count ceros on each nums and sum of each nums
        # there are 3 cases:
        #   if  sum_nums1 > sum_nums2:
        # ceros_nums1  ......

        sum_nums1 = sum(nums1)
        sum_nums2 = sum(nums2)
        ceros_nums1 = nums1.count(0)
        ceros_nums2 = nums2.count(0)


        #case 0:
        if ceros_nums1 == 0 and ceros_nums2 == 0 and sum_nums1 !=sum_nums2 :
            return -1

        #case 1:
        if ceros_nums1 == 0:
            if sum_nums2+ceros_nums2 <= sum_nums1:
                return sum_nums1
            else:
                return -1
        #case 2:
        if ceros_nums2 == 0:
            if sum_nums1+ceros_nums1 <= sum_nums2:
                return sum_nums2
            else:
                return -1

        #case 3:
        return max(sum_nums1+ceros_nums1,sum_nums2+ceros_nums2)
