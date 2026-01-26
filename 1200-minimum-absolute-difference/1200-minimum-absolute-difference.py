class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:



        #aproach:
        # sort , min absolut dist is always between adjacent elments

        arr.sort()
        min_diff = float("inf")
        ans = []
        for i in range(len(arr)-1):
            curr_min = arr[i+1]-arr[i]
            if curr_min < min_diff:
                ans = [ [arr[i],arr[i+1]] ]
                min_diff = curr_min
            elif curr_min == min_diff:
                ans.append([arr[i],arr[i+1]])

        return ans

        