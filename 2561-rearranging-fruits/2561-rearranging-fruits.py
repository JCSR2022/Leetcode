class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        #first problem is to check if baskets can be equal
        #secund check what changes need to be done

        #try some kind of bisextion?
        #basket1 = [4,2,2,2], basket2 = [1,4,1,2]
        #t_b1 = 10 and t_b2 = 8 , tb1> tb2 ,dif == 2
        # 
        #no, me rindo hoy no sirvo para una mierda!!!!
        #Thanks Muthu Vrn
        
        cnt = Counter(basket1)
        for x in basket2: cnt[x] -= 1
        last = []
        for k, v in cnt.items():
            # if v is odd, an even distribution is never possible
            if v % 2 != 0:
                return -1
            # the count of transferred k is |v|/2
            last += [k] * abs(v // 2)
        # find the min of two input arrays as the intermediate
        minx = min(basket1 + basket2)
        # Use quickselect instead of sort can get a better complexity
        last.sort()
        # The first half may be the cost
        return sum(min(2*minx, x) for x in last[0:len(last)//2])

