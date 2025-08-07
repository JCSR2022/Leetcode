
class SegTree:
    
    def __init__(self,arr):
        
        self.size = len(arr)
        self.arr = arr
        self.seg_tree = [-1] * (4 * self.size) 
        self.construct_segment_tree(0,0,self.size-1)
        
    def construct_segment_tree(self,i, l_idx, r_idx):
        if l_idx == r_idx:
            self.seg_tree[i] = self.arr[l_idx]
            return self.seg_tree[i]
        
        mid = (l_idx + r_idx) // 2
        left_max = self.construct_segment_tree(2 * i + 1, l_idx, mid)
        right_max = self.construct_segment_tree(2 * i + 2, mid + 1, r_idx)
        self.seg_tree[i] = max(left_max, right_max)
        return self.seg_tree[i]
    
    def find_left_max_idx(self,i,l_idx,r_idx,num):
        
        if  self.seg_tree[i] < num:
            return -1
        
        if l_idx == r_idx: 
            self.seg_tree[i] = -1
            self.arr[l_idx] =-1
            return l_idx 
        
        
        mid = (l_idx + r_idx) // 2
        left = self.find_left_max_idx(2*i+1, l_idx, mid,num)
        if left >= 0:
            self.seg_tree[i] = max(self.seg_tree[2*i+1],self.seg_tree[2*i+2])  
            return left
        
        right =self.find_left_max_idx(2*i+2, mid+1, r_idx,num)
        if right >= 0:
            self.seg_tree[i] = max(self.seg_tree[2*i+1],self.seg_tree[2*i+2]) 
            return right
        
        return -1


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        

        #this was yesterday sol, O(n**2)
        # N = len(fruits)
        # ans = 0 
        # for fruit in fruits:
        #     for i in range(N):
        #         if baskets[i] >= fruit:
        #             baskets[i] = -1
        #             break
        #     else:
        #         ans +=1
        # return ans
        #diff between yesterday is size n**5..will not work for time

#Time Limit Exceeded as expected
#---------------------------------------
        #Lets try sort basket and use bisection  O(nlogn)
        # N = len(fruits)
        # baskets.sort()  
        # ans = 0

        # for fruit in fruits:
        #     print(baskets)
        #     l = 0
        #     r = len(baskets)-1
        #     fruit_idx = -1
        #     while l<=r:
        #         m =  (l+r)//2
        #         print(fruit,l,m,r,baskets[m],baskets[m] < fruit,fruit_idx,ans )
        #         if baskets[m] < fruit:
        #             l = m + 1        
        #         else:
        #             fruit_idx = m
        #             r = m - 1

        #     if fruit_idx == -1:
        #         ans +=1
        #     else:
        #         print("fruit_idx:",fruit_idx,"baskets[fruit_idx]:",baskets[fruit_idx] )
        #         del baskets[fruit_idx]

        # return ans

#no funciona
#------------------------------------------------------------------------
        #usar un heap??
    
        # bask_idx = [(i,v) for i,v in enumerate(baskets)]  
        # heapq.heapify(bask_idx)
        # ans = 0

        # for fruit in fruits:
        #     #print(bask_idx)
        #     temp = []
        #     while bask_idx and bask_idx[0][1] < fruit:
        #         heapq.heappush(temp, heapq.heappop(bask_idx))

        #     if bask_idx:
        #         heapq.heappop(bask_idx)
        #         while temp:
        #             heapq.heappush(bask_idx,heapq.heappop(temp))
        #     else:
        #         bask_idx = temp
        #         ans +=1


        # return ans

#Time Limit Exceeded the same,
#--------------------------------------------------------------------
        #using SegTree!!!

        mySegTree = SegTree(baskets)
        ans = 0
        for fruit in fruits:
            if mySegTree.find_left_max_idx(0,0,mySegTree.size-1, fruit) < 0:
                ans += 1

        return ans








