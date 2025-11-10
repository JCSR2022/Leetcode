class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        #try  : [2,3,2,1,3,2,3,1]
        # 1. [2,3,2,0,3,2,3,0]
        # 2. [0,3,0,0,3,2,3,0]
        # 3. [0,3,0,0,3,0,3,0]
        # 4. [0,0,0,0,3,0,3,0]
        # 5. [0,0,0,0,0,0,3,0]
        # 6. [0,0,0,0,0,0,0,0]

        # aproach , recursive? can not be n**2 will not work:
        # find min , make split on min return count on each split +1

        # def splitArr(curr_arr,curr_min):
        #     # Split the list 
        #     result = []
        #     temp = []
        #     for num in curr_arr:
        #         if num == curr_min:
        #             if temp:      
        #                 result.append(temp)
        #                 temp = []
        #         else:
        #             temp.append(num)

        #     # Add the last group if it exists
        #     if temp:
        #         result.append(temp)

        #     #print(result)
        #     return result


        # heap = list(set(nums))
        # heapq.heapify(heap)

        # arrs = splitArr(nums,0)
        # count = 0
        # while heap:
        #     curr_min = heapq.heappop(heap)
        #     new_arr = []
        #     for curr_arr in arrs:
        #         if curr_min in curr_arr: count +=1
        #         new_arr += splitArr(curr_arr,curr_min)
        #     arrs = new_arr

      
        # return count

#Time Limit Exceeded
#-------------------------------------------------------------------



        # def split_indexes(arr, val):
        #     """
        #     Instead of creating subarrays, return a list of (start, end)
        #     index ranges that represent segments of arr separated by val.
        #     """
        #     segments = []
        #     start = 0
        #     n = len(arr)
        #     for i, x in enumerate(arr):
        #         if x == val:
        #             if start < i:
        #                 segments.append((start, i))  # segment [start, i)
        #             start = i + 1
        #     if start < n:
        #         segments.append((start, n))  # last segment
        #     return segments

        # # Build min-heap of unique values
        # heap = list(set(nums))
        # heapq.heapify(heap)

        # # Start with one big segment covering the entire array
        # segments = [(0, len(nums))]
        # count = 0

        # while heap:
        #     curr_min = heapq.heappop(heap)
        #     new_segments = []

        #     for start, end in segments:
        #         # Check if curr_min is inside this slice
        #         if curr_min in nums[start:end]:
        #             count += 1
        #         # Split the segment based on curr_min positions
        #         new_segments += split_indexes(nums[start:end], curr_min)
        #         # Adjust indexes back to global array positions
        #         new_segments = [(start + s, start + e) for s, e in new_segments]

        #     segments = new_segments

        # return count

# no esperaba nada de ti chat GPT pero igual me decepcionaste
#--------------------------------------------------------------------
        #https://www.youtube.com/watch?v=s9-gPx1Nvho
        #Usign a monotonic stack

        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            
            # if n == 0:
            #     continue

            if n > 0 and (not stack or n > stack[-1]) :
                res += 1
                stack.append(n)

        return res




