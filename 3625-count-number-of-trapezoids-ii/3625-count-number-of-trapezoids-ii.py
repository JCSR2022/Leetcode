from itertools import combinations

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        #brute force:

        #dos rectas paralelas tienen la misma pendiente
        #m = (y1-y0)/(x1-x0)
        # necesitamos todas las pendientes posibles?
        # todos los posibles pares de puntos seria max comb(2,points.length=500) = 124.750, 
        # hash de pendientes (ojo x1==x2) y se guarda un set con los cruces por el eje y,
        # y-y0 = m*(x-x0) .... y = m*x0+y0
        # identificando todas las rectas paralelas

        # #just for a better visualization:
        # p_dict = { p:point for p,point in enumerate(points) }
        # #print(p_dict)
        # #print()

        # hash_slope = defaultdict(lambda: defaultdict(set))
        # for  P1,P0 in combinations(p_dict.keys(),2):
        #     if p_dict[P1][0] == p_dict[P0][0]:
        #         m = 'y' 
        #         cross = p_dict[P1][0]
        #     else:
        #         m =  (p_dict[P1][1] - p_dict[P0][1])/(p_dict[P1][0] - p_dict[P0][0])
        #         cross = round(p_dict[P0][1] - m*p_dict[P0][0],4)

        #     hash_slope[m][cross].add(P0)
        #     hash_slope[m][cross].add(P1)

    

        # ans = []

        # for k,v in hash_slope.items():
        #     if len(v)>1:
        #         set_combs = list(v.values())
        #         #print()
        #         #print(k,set_combs)
        #         #print(k,dict(v))

        #         point_combs = [ [set(comb) for comb in combinations(s, 2)] for s in set_combs]
        #         size = len(point_combs)
                
        #         for i in range(size):
        #             for j in range(i+1,size):
        #                 for p1 in point_combs[i]:
        #                     for p2 in point_combs[j]:
        #                         curr_pol = p1|p2
        #                         if curr_pol not in ans:
        #                             ans.append(curr_pol)
        #                             #print(curr_pol)
                    
        # # ans = 0
        # # for v in hash_slope.values():
        # #     if len(v)>1:
        # #         print(list(v.values()))
        # #         print([len(p) for p in  v.values()])
        # #         points_comb = [math.comb(len(p), 2)  for p in  v.values()]
        # #         print(points_comb)
        # #         prev = 0
        # #         for cur_pare in points_comb:
        # #             ans += prev*cur_pare
        # #             prev += cur_pare
        # #         print(ans)

        # #print([ [p_dict[p] for p in points ] for points in  ans])
        # return len(ans)

#Time Limit Exceeded  @#%#^$%$^#$%&#&^%&$^&$%
#---------------------------------------------------------------


        # p_dict = { p:point for p,point in enumerate(points) }

        # def checkSlope(cur_pts, p_dict, tol=1e-4):
        #     """Check if a 4-point polygon has 2 parallel sides."""

        #     def slope(p1, p2):
        #         """Compute slope between two points."""
        #         x1, y1 = p1
        #         x2, y2 = p2
                
        #         if x2 == x1:        # vertical line
        #             return float('inf')
        #         return (y2 - y1) / (x2 - x1)

        #     p0, p1, p2, p3 = [p_dict[i] for i in cur_pts]
            
        #     # Slopes of opposite sides
        #     m1 = slope(p0, p1)
        #     m2 = slope(p2, p3)

        #     m3 = slope(p0, p2)
        #     m4 = slope(p1, p3)

        #     return isclose(m1, m2, rel_tol=tol) or isclose(m3, m4, rel_tol=tol)


        # ans = 0
        # for cur_pts in combinations(p_dict.keys(),4):
        #     if checkSlope(cur_pts,p_dict):
        #         ans += 1 

        # return ans

#-----------------------------------------------------------------------



        def checkSlope(cur_pts, tol=1e-4):
            """Check if a 4-point polygon has 2 parallel sides."""

            def slope(p1, p2):
                """Compute slope between two points."""
                x1, y1 = p1
                x2, y2 = p2
                
                if x2 == x1:        # vertical line
                    return float('inf')
                return (y2 - y1) / (x2 - x1)

            allx,ally = zip(*cur_pts) 
            if len(set(allx)) < 2 or len(set(ally)) < 2:
                return False 

            p0, p1, p2, p3 = [p for p in cur_pts]
            
            # Slopes of opposite sides
            m1 = slope(p0, p1)
            m2 = slope(p2, p3)

            m3 = slope(p0, p2)
            m4 = slope(p1, p3)

            m5 = slope(p0,p3)
            m6 = slope(p1,p2)

            return (isclose(m1, m2, rel_tol=tol) or 
                    isclose(m3, m4, rel_tol=tol) or
                    isclose(m5, m6, rel_tol=tol))


        ans = 0
        for cur_pts in combinations(points,4):
            #print(cur_pts,checkSlope(cur_pts))
            if checkSlope(cur_pts):
                ans += 1 

        return ans




        