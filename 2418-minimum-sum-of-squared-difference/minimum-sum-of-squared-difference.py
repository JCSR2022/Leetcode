class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:



        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        remaining = k - sum(
            max(0, d - threshold) for d in diff
        )

        result = 0

        for d in diff:
            d = min(d, threshold)

            if d == threshold and remaining > 0:
                d -= 1
                remaining -= 1

            result += d * d

        return result











#------------------------------------------------------------------------
        # heap = []
        # for a, b in zip(nums1, nums2):
        #     heapq.heappush(heap,-abs(a-b))

        # k = k1+k2
        # while heap[0]>0 and k>0:
        #     curr_max = - heapq.heappop(heap)
        #     heapq.heappush(heap,-(curr_max**2-2*curr_max+1))

    
        # return sum( n**2 for n in heap)
    #maldito imbecil!!!!!!!!!!!!!!!!!!!11


#--------------------------------------------------------------------------------
#         n = len(nums1)
#         heap =[]
        
#         for i in range(n):
#             heapq.heappush(heap, (-abs(nums1[i] - nums2[i]), i))



#         while k1 > 0 and heap[0][0] < 0:
#             _ , i = heapq.heappop(heap)
#             if nums1[i] > nums2[i]:
#                 nums1[i] -= 1
#             else:
#                 nums1[i] += 1
#             k1 -= 1
#             heapq.heappush(heap, (-abs(nums1[i] - nums2[i]), i))


#         while k2 > 0 and heap[0][0] < 0:
#             _ , i = heapq.heappop(heap)
#             if nums2[i] > nums1[i]:
#                 nums2[i] -= 1
#             else:
#                 nums2[i] += 1
#             k2 -= 1
#             heapq.heappush(heap, (-abs(nums1[i] - nums2[i]), i))

#         return sum((a - b)**2 for a, b in zip(nums1, nums2))


# #Time Limit Exceeded