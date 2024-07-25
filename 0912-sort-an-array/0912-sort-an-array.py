class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort
        #divide , sort and merge
        
        
        def divide(chunk):
            size = len(chunk)
            if size >= 2:
                left = chunk[:size//2]
                right = chunk[size//2:]
                return left, right
            else:
                return chunk, []
        
        def merge(left,right):
            p_l = 0
            p_r = 0
            ans = []
            while p_r < len(right) and p_l < len(left) :               
                if left[p_l] > right[p_r]:
                    ans.append(right[p_r])
                    p_r += 1
                else:
                    ans.append(left[p_l])
                    p_l += 1
            if p_r <= len(right):
                ans += right[p_r:]
            if p_l <= len(left):
                ans += left[p_l:]
            
            return ans
            
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            left, right = divide(arr)
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)
                
        
        return merge_sort(nums)
        
            