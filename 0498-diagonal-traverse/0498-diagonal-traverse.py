class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])
        ans = []
        i = 0
        j = 0
        up = True
        #while i < m-1 or j < n-1  :
        while i < m and j < n :   

            ans.append(mat[i][j])
            #print(i,j,up,ans)
            if up:
                #diagonal up
                if i-1 >= 0 and j+1 <= n-1:  
                    i -=1
                    j +=1
                #reach top, go to next colum
                elif i-1 < 0 and j+1 <= n-1:
                    j +=1
                    up = False
                #reach right, got next row
                elif j+1 > n-1:
                    i += 1
                    up = False
            else:
                #diagonal down
                if i+1 <= m-1 and j-1 >= 0:
                    i += 1
                    j -= 1
                #reach left, go to next row
                elif i+1 <= m-1 and j-1 < 0:
                    i += 1
                    up =True
                #reach bottom, go to nex colum
                elif i+1 > m-1:
                    j += 1
                    up =True
            #print("    next:",i,j)

        #ans.append(mat[i][j])

        return ans




        


        