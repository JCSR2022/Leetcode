class SegTree:
    
    def __init__(self,arr):

        self.size = len(arr)
        self.arr = arr
        self.seg_tree = [0] * (4 * self.size) 
        self.construct_segment_tree(0,0,self.size-1)
        
    def construct_segment_tree(self,i, l_idx, r_idx):
        if l_idx == r_idx:
            self.seg_tree[i] = self.arr[l_idx]
            return self.seg_tree[i]

        mid = (l_idx + r_idx) // 2
        left_sum = self.construct_segment_tree(2 * i + 1, l_idx, mid)
        right_sum = self.construct_segment_tree(2 * i + 2, mid + 1, r_idx)

        self.seg_tree[i] = left_sum + right_sum
        return self.seg_tree[i]
    
    
    def update(self, index, val):
        diff = val - self.arr[index]
        self.arr[index] = val

        def tree_update(i, curr_l_idx, curr_r_idx):

            if index < curr_l_idx or index > curr_r_idx:
                return

            self.seg_tree[i] += diff

            if curr_l_idx == curr_r_idx:
                return

            mid = (curr_l_idx + curr_r_idx) // 2
            tree_update(2*i+1, curr_l_idx, mid)
            tree_update(2*i+2, mid+1, curr_r_idx)

        tree_update(0, 0, self.size-1)
        
        
    def query_sum(self,cnt, i, curr_l_idx, curr_r_idx, ql, qr):

        if qr < curr_l_idx or ql > curr_r_idx:
            return 0
        
        if ql <= curr_l_idx and curr_r_idx <= qr:
            return self.seg_tree[i]
        
        mid = (curr_l_idx + curr_r_idx) // 2
        left_sum = self.query_sum(cnt+2,2*i+1, curr_l_idx, mid, ql, qr)
        right_sum = self.query_sum(cnt+2,2*i+2, mid+1, curr_r_idx, ql, qr)
        return left_sum+right_sum

    
class NumArray:

    def __init__(self, nums: List[int]):
        self.mySegTree = SegTree(nums)
        

    def update(self, index: int, val: int) -> None:
        self.mySegTree.update(index,val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.mySegTree.query_sum(0,0,0,self.mySegTree.size-1,left,right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)