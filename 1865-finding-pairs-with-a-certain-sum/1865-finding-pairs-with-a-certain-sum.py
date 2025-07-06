class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        
        self.nums1 = nums1
        self.nums2 = nums2

        self.val_nums2 = {}
        for n2 in nums2:
            if n2 in self.val_nums2:
                self.val_nums2[n2] +=1
            else:
                self.val_nums2[n2] = 1

    def add(self, index: int, val: int) -> None:
            self.val_nums2[self.nums2[index]] -=1
            self.nums2[index] += val
            if self.nums2[index] in self.val_nums2:
                self.val_nums2[self.nums2[index]] +=1
            else:
                self.val_nums2[self.nums2[index]] = 1

                
    def count(self, tot: int) -> int:
        ans = 0
        for n1 in self.nums1:
            need_n2 = tot-n1
            if need_n2 in self.val_nums2:
                ans +=  self.val_nums2[need_n2]
        return ans
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)




#----------------------------------------------------------------------
#----------------------------------------------------------------------
# #Time Limit Exceeded
# class FindSumPairs:

#     def __init__(self, nums1: List[int], nums2: List[int]):
#         self.nums1 = nums1
#         self.nums2 = nums2
#         self.sum_idx = defaultdict(lambda: defaultdict(int))
#         self.idx_sum = defaultdict(set)
#         for i in range(len(self.nums1)):
#             for j in range(len(self.nums2)):
#                self.sum_idx[self.nums1[i]+self.nums2[j]][j] +=1 
#                self.idx_sum[j].add(self.nums1[i]+self.nums2[j])
#         #self.print_data()
    
#     def print_data(self):
#         for k,v in self.sum_idx.items():
#             print(k,dict(v))
#         print()
#         print(dict(self.idx_sum))
#         print()

#     def add(self, index: int, val: int) -> None:
#         self.nums2[index] += val
        
#         for cur_sum in self.idx_sum[index]:
#             self.sum_idx[cur_sum][index] = 0
        
#         self.idx_sum[index] = set()
#         for i in range(len(self.nums1)):
#             curr_sum = self.nums1[i]+self.nums2[index]
#             self.sum_idx[curr_sum][index] +=1
#             self.idx_sum[index].add(curr_sum)

#         #print(f"change: index:{index}, val:{val}")
#         #self.print_data()

#     def count(self, tot: int) -> int:
#         return sum(self.sum_idx[tot].values() )



