class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        arr = [[1]]

        if numRows == 1:
            return arr
        
        
        for _ in range(numRows-1):
            curr_arr = [0] + arr[-1] + [0]
            new_arr = []
            for i in range(len(curr_arr)-1):
                 new_arr.append(curr_arr[i]+curr_arr[i+1])
            arr.append(new_arr)

        return arr

        