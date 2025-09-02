class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        # brute force: build dit with x values as keys , y values as val

        #


        dict_points = defaultdict(list)
        for x, y in points:
            heapq.heappush(dict_points[x], -y)

        x_sort = sorted(dict_points.keys())
        n = len(x_sort)


        for x in x_sort:
            print(x,[-cur_x for cur_x in dict_points[x]])
        print()

        ans = 0
        for i,x in enumerate(x_sort):
            left_heap = dict_points[x] 
            while left_heap:
                if len(left_heap) > 1: 
                    ans +=1
                    print(left_heap)
                top_left = -heapq.heappop(left_heap)
                min_y = 0
                for j in range(i+1,n):
                    x_heap = dict_points[x_sort[j]]
                    for y in x_heap:
                        if min_y  < -y <= top_left:
                            ans +=1
                            print( (x,top_left ),((x_sort[j],-y ),x_heap ) )
                            min_y = -y
                            break
            print()
        
        return ans