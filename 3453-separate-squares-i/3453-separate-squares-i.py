class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:



        
        def check(target):
            top = 0
            bot = 0

            for x,y,size in squares:
                top_limit = y + size
                bot_limit = y

                if  bot_limit <= target <= top_limit:
                    top += (top_limit-target)*size
                    bot += (target - bot_limit)*size
                elif target < bot_limit:
                    top += size**2
                elif target > top_limit:
                    bot += size **2

            return top-bot 


        l = float("inf")
        h = 0 
        for x,y,size in  squares:
            l = min(l,y)
            h = max(h, y+size)

        #bisect
        while h-l > 10**(-5):
            mid = l + (h-l)/2
            if check(mid) > 0:
                l = mid 
            else:
                h = mid
        
        return h
            
              















        # squares.sort(key=lambda x: x[1] )

        # def findYArea(y):
        #     int_y = int(y)
        #     cur_y = 0
        #     area = 0
        #     i = 0
        #     while cur_y <= int_y  
        #         area += squares[i][2]**2 
        #         i +=1
        #         cur_y = squares[i][1]
                

        # return 1
        


