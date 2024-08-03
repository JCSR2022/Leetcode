class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

        if len(target) != len(arr):
            return False

        elementCounts = [0] * 1001

        for targetNum, currentNum in zip(target, arr):
            elementCounts[targetNum] += 1
            elementCounts[currentNum] -= 1

        return all(count == 0 for count in elementCounts)
        
#         c_arr = Counter(arr)
#         c_target = Counter(target)
        
#         return c_target==c_arr
        