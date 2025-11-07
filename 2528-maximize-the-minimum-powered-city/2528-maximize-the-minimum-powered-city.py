
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        
        #brute force

        # cnt_sta = len(stations)
        # min_power =[ sum(stations[max(0,i-r):min(cnt_sta, i+r+1)])   for i in range(cnt_sta) ]

        # print("min_power",min_power)

        # for _ in range(k):
        #     indx = min_power.index(min(min_power))
        #     # if indx == 0 and cnt_sta > 1: indx = 1
        #     # if indx == cnt_sta-1 and cnt_sta > 1: indx = cnt_sta-2
        #     print("indx",indx)
        #     for idiff in range(-r,r+1):
        #         imod = indx + idiff 
        #         if  imod>= 0 and imod < cnt_sta:
        #             min_power[imod] +=1
        #     print(min_power)
            
        # return min(min_power)

#is not working do to insted of upgrade the min, can upgrade in between mins//
#------------------------------------------------------------------------------

#solution Binary search, sliding window!!!??/ Go FYself
#https://www.youtube.com/watch?v=E6aEq7V9TDk

        lo = min(stations)
        hi = sum(stations)+k

        stations = [0]*r + stations + [0]*r
        res = lo


        def check(med):
            available = k 
            ind = r
            window = sum(stations[:2*r])
            added = defaultdict(int)

            while ind  < len(stations) - r:
                window += stations[ind+r]
                
                if window < med:
                    diff = med - window 
                    if diff > available:
                        return False

                    window += diff
                    added[ind+r] =diff
                    available -=diff 

                window -= (stations[ind-r] + added[ind-r])
                ind += 1
            return True




        while lo <= hi:
            m = (lo+hi)//2
            if check(m):
                res = m
                lo = m+1
            else:
                hi = m-1

        return res














        







