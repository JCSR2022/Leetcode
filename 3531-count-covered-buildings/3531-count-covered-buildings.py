class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        #aproach
        # create matrix ceros
        # use a code to check if l,r,u,d [8,4,2,1] as binary [0 0 0 0]
        # move for each , create 4 matrices?
        #noooooo

        #create matrix
        #sort buildings


        #make 2 dicts x:ys and y:xs

        # x_arr = defaultdict(list)
        # y_arr = defaultdict(list)

        
        # for x,y in buildings:
        #     x_arr[x].append(y)
        #     y_arr[y].append(x)
        # print(dict(x_arr))
        # print(dict(y_arr))


        # ys_to_review = set()
        # for x,ys in x_arr.items():
        #     if len(ys) > 2:
        #         ys.sort()
        #         ys_to_review = ys_to_review|set(ys[1:-1])
        # print(ys_to_review)
        # ans = 0
        # for ys in ys_to_review:
        #     curr_ys = len(y_arr[ys])
        #     if curr_ys > 2:
        #         ans += curr_ys-2

        # return ans 

#vete a la mierda, toda la logica esta mal!!!!
#--------------------------------------------------------



        # rmax = [0] * (n + 1)
        # rmin = [n + 1] * (n + 1)
        # cmax = [0] * (n + 1)
        # cmin = [n + 1] * (n + 1)

        # # Track extreme buildings for each row and column
        # for x, y in buildings:
        #     rmax[y] = max(rmax[y], x)
        #     rmin[y] = min(rmin[y], x)
        #     cmax[x] = max(cmax[x], y)
        #     cmin[x] = min(cmin[x], y)

        # ans = 0

        # # A building is covered only if it's strictly inside both extremes
        # for x, y in buildings:
        #     if rmin[y] < x < rmax[y] and cmin[x] < y < cmax[x]:
        #         ans += 1

        # return ans
            


#-----------------------------------------------------------------------------------



        x_arr = defaultdict(list)
        y_arr = defaultdict(list)

        
        for x,y in buildings:
            x_arr[x].append(y)
            y_arr[y].append(x)
        # print(dict(x_arr))
        # print(dict(y_arr))

        for x,ys in x_arr.items():
            if len(ys) > 2:
                ys.sort()
                x_arr[x] = ys[1:-1]
            else:
                x_arr[x] = []
        
        for y,xs in y_arr.items():
            if len(xs) > 2:
                xs.sort()
                y_arr[y] = xs[1:-1]
            else:
                y_arr[y] = []


        # print(dict(x_arr))
        # print(dict(y_arr))

        
        ans = 0
        for x,ys in x_arr.items():
            if ys:
                for y in ys:
                    if x in y_arr[y]:
                        ans +=1
        return ans 
