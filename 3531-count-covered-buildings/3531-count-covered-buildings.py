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

        x_arr = defaultdict(list)
        y_arr = defaultdict(list)

        for x,y in buildings:
            x_arr[x].append(y)
            y_arr[y].append(x)

        ys_to_review = set()
        for x,ys in x_arr.items():
            if len(ys) > 2:
                ys.sort()
                ys_to_review = ys_to_review|set(ys[1:-1])

        ans = 0
        for ys in ys_to_review:
            curr_ys = len(y_arr[ys])
            if curr_ys > 2:
                ans += curr_ys-2

        return ans 



            



