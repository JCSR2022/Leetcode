class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:




        def checkFirst(start1,duration1,start2,duration2):
            finish_1 = float('inf')
            for i in range(len(start1)):
                finish_1 = min(finish_1, start1[i] + duration1[i])

            finish_2 = float('inf')
            for i in range(len(start2)):
                finish_2 = min(finish_2, max(finish_1,start2[i]) + duration2[i])

            return finish_2

        begin_land = checkFirst(landStartTime,landDuration,waterStartTime,waterDuration)
        begin_water = checkFirst(waterStartTime,waterDuration,landStartTime,landDuration)
        return min( begin_land ,begin_water )

        