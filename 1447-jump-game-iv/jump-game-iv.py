class Solution:
    def minJumps(self, arr: List[int]) -> int:
        #brute force

        index_values = defaultdict(set)
        for i,num in enumerate(arr):
            index_values[num].add(i)

        limit = len(arr)
        heap = [(0,0)]
        visited_nums = set()
        visited_idx = set()

        while heap:
            steps,curr_idx = heapq.heappop(heap)

            if curr_idx == limit-1:
                return steps

            right = curr_idx+1
            if  right < limit and right not in visited_idx:
                visited_idx.add(right)
                heapq.heappush(heap, (steps+1,right) )
             
            left = curr_idx-1
            if left > 0 and left not in visited_idx:
                visited_idx.add(left)
                heapq.heappush(heap, (steps+1,left))

            if arr[curr_idx] not in visited_nums:
                visited_nums.add(arr[curr_idx])
                for jump_idx in index_values[arr[curr_idx]]:
                    visited_idx.add(jump_idx)
                    heapq.heappush(heap, (steps+1,jump_idx))
            











            