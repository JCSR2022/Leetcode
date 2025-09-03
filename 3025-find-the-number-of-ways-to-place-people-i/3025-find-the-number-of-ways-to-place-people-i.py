class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        # brute force: build dit with x values as keys , y values as val

        #


        # dict_points = defaultdict(list)
        # for x, y in points:
        #     heapq.heappush(dict_points[x], -y)

        # x_sort = sorted(dict_points.keys())
        # n = len(x_sort)


        # for x in x_sort:
        #     print(x,[-cur_x for cur_x in dict_points[x]])
        # print()

        # ans = 0
        # for i,x in enumerate(x_sort):
        #     left_heap = dict_points[x] 
        #     while left_heap:
        #         if len(left_heap) > 1: 
        #             ans +=1
        #             print(left_heap,"vertical")
        #         top_left = -heapq.heappop(left_heap)
        #         min_y = 0
        #         for j in range(i+1,n):
        #             x_heap = dict_points[x_sort[j]]
        #             for y in x_heap:
        #                 if min_y  < -y <= top_left:
        #                     ans +=1
        #                     print( (x,top_left ),((x_sort[j],-y ),[ -k for k in x_heap] ) )
        #                     min_y = -y
        #                     break
        #     print()
        
        # return ans

#no funciona por que eres un Q#$@%@%@#%@#%@$^#&%^*^%*&(O*())
#------------------------------------------------------------------
        points.sort(key=lambda x: (x[0], -x[1]))
        #print(points)
        n = len(points)
        ans = 0

        for i,(xa,ya) in enumerate(points):
            #print(i,(xa,ya))
            cur_y_min = 0 
            while i < n-1 and cur_y_min < ya:
                i += 1
                cur_y = points[i][1]
                if  cur_y > cur_y_min and cur_y <= ya :
                    ans +=1
                    cur_y_min = cur_y

                #print("##",j,points[j],cur_y ,cur_y_min,cur_y <= cur_y_min,ans)

        return ans


































    #vete a la maldita mierda!!!!!
        # points.sort(key=lambda x: (x[0], -x[1]))
        # cnt = 0
        # for i in range(len(points) - 1):
        #     x, y = points[i]
        #     lower = -1
        #     for j in range(i + 1, len(points)):
        #         if lower < points[j][1] <= y:
        #             cnt += 1
        #             lower = points[j][1]
        #         if lower == y: break
        # return cnt